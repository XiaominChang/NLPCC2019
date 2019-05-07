# NLPCC2019
### NLP2019评测任务的服务模板和评测方案，具体请见docx文档  

ServerDemo.py: 搭建服务的代码，默认端口2019 (若更换端口则修改该文件，并告知组织方)，无需修改。  

RequestHandlerDemo.py: 参评者需修改该文件内部的getReply(self, sentence) 函数，在内部得到单句对话回答并返回。若参评者想获取批量对话应答结果，也可修改getBatchReplies(self, sentencesList) 函数，函数说明见内部注释。  

testDemo.py: 该文件用于给参评者自行测试服务是否能够顺利跑通，用了python的requests包编写，当把服务搭建在服务器上后，修改testDemo.py内部的url地址，然后在其他任意连接公网的网络运行testDemo.py文件，模拟组织方向参评者服务器发送对话请求。其中single_test()用于单句测, multi_test()用于多句测试。
