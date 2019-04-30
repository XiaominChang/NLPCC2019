# -*- coding: utf-8 -*-
import requests
import json

class RequestHandler():

    def __init__(self):
        pass

    def getReply(self, sentence):
        """1. Reply based on a given sentence

        Args:
            sentence: A string of sentence.

        Returns:
            sentence: A string of sentence.
        """

        return "reply"

    def getBatchReplies(self, sentencesList):
        """2. Reply to a batch of sentences

        Args:
            sentencesList: A List of Dictionaries of ids and sentences,
                like:
                [{'id':331, 'content':'今天天气不错' },
                 {'id':332, 'content':'今天好冷啊' },
                 ... ]

        Returns:
            resultsList: A List of Dictionaries of ids and replies.
                The order of the list must be the same as the input list,
                like:
                [{'id':331, 'result':'挺好的' },
                 {'id':332, 'result':'咱们去吃火锅吧' },
                 ... ]
        """
        repliesList = []
        for sentence in sentencesList:
            replyDict = {}
            replyDict['qid'] = sentence['qid']
            try:
                replyDict['question'] = self.getReply(sentence['question'])
                repliesList.append(replyDict)
            except Exception as e:
                print Exception, ' : ', e
        return repliesList