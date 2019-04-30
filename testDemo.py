# -*- coding: utf-8 -*-
import time
import requests
import json


def single_test():
    """
    此函数为测试函数，将ServerDemo.py运行在服务器端后，用该程序在另一网络测试
    此函数适用于单个问题测试
    """

    # 此URL中IP地址为参赛者的服务器地址，应为可达的公网IP地址，端口默认2019
    url = 'http://0.0.0.0:2019/nlpcc_2019/query'
    uid = "123456"
    sentence = '你叫什么名字'
    headers = {'Content-type': 'application/json'}
    try:
        r = requests.get(url, params={'uid': uid, 'q': sentence}, headers=headers, timeout=4)
        if r.status_code == 200:
            data = r.json()
            print data['uid'], data['answer']
        else:
            print "wrong,status_code: ", r.status_code
    except Exception as e:
        print Exception, ' : ', e


def multi_test():
    """
    此函数为测试函数，将ServerDemo.py运行在服务器端后，用该程序在另一网络测试
    此函数适用于问题集测试
    """

    url = "http://0.0.0.0:2019/nlpcc_2019"

    sentencesList = [{'qid': 121, 'question': '你好'},
                     {'qid': 122, 'question': '你叫什么名字'},
                     {'qid': 123, 'question': '明天天怎么样'}]
    sentences = {'questionSet': sentencesList}
    headers = {'Content-type': 'application/json'}
    try:
        r = requests.post(url, data=json.dumps(
            sentences), headers=headers, timeout=4)
        if r.status_code == 200:
            data = r.json()
            repliesList = data['resultSet']
            for reply in repliesList:
                print reply['qid'], reply['question']
        else:
            print "wrong,status_code: ", r.status_code
    except Exception as e:
        print Exception, ' : ', e


if __name__ == '__main__':
    single_Test()
    multi_Test()
