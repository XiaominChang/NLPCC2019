# -*- coding: UTF-8 -*-
from flask import Flask, jsonify, request, session
from RequestHandlerDemo import RequestHandler
import hashlib
from datetime import timedelta

app = Flask(__name__)
Handler = RequestHandler()
key = "123456"


@app.route('/nlpcc_2019/query', methods=['GET'])
def returnGet():
    sentence = request.values.get('q')
    uid = request.values.get('uid')
    reply = Handler.getReply(sentence)
    return jsonify({'answer': reply, 'uid': uid})


@app.route('/nlpcc_2019', methods=['POST'])
def returnPost():
    print request.get_json()
    sentencesList = request.json.get('questionSet')
    repliesList = Handler.getBatchReplies(sentencesList)
    return jsonify({'resultSet': repliesList})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2019)
