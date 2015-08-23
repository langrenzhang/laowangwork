#coding=utf-8
import threading
import time
import re
import urllib
import bs4
'''


多线程爬虫

1.抓什么？怎么抓？ -》 确定抓取流程
2.爬虫的第一步是分析
3.分析的工具 firebug
4.urllib足矣，还有scrapy
5.分析数据，正则 or beautifulsoup
6.beautifulsoup的小入门
7.如何让
8.接下来靠你了




这次习题：
作业1：

url :"http://money.163.com/special/pinglun/"
抓取第一页的新闻信息，并按照以下规格输出。

[

  {'title':'生鲜电商为何难盈利？','created_at':'2013-05-03 08:43','url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}

  {'title':'生鲜电商为何难盈利？','created_at':'2013-05-03 08:43','url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}


]


作业3：

使用beatifulsoup完成作业1的要求.

'''



'''
作业4：

使用scrapy完成作业2的需求。

jd_search(keyword,page_skip=1,page_limit=10) #抓1后面10页（包括第10页）的内容。
jd_search(keyword,page_skip=4,page_limit=3) #抓4后面3页（包括第6页）的内容。

'''