#coding=utf-8
#! /usr/bin/python
#py2.7

#import threading
#import time
import re
import urllib
from bs4 import BeautifulSoup
#import socket

'''
hui tou jie zhe zuo lian xi ti 

多线程爬虫

1.抓什么？怎么抓？ -》 确定抓取流程
2.爬虫的第一步是分析
3.分析的工具 firebug
4.urllib足矣，还有scrapy
5.分析数据，正则 or beautifulsoup
6.beautifulsoup的小入门
7.如何让
8.接下来靠你了

ps:mashup,firebug

'''

'''
作业1：

url :"http://money.163.com/special/pinglun/"
抓取第一页的新闻信息，并按照以下规格输出。

[

  {'title':'生鲜电商为何难盈利？','created_at':'2013-05-03 08:43','url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}

  {'title':'生鲜电商为何难盈利？','created_at':'2013-05-03 08:43','url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}


]

'''
   
url = "http://money.163.com/special/pinglun/"
#url = "http://www.zhihu.com/question/22576739"
#print caturl(url)
 
#<a href="http://money.163.com/15/0826/11/B1UM4HEB00253G87.html" title="国产手机端保形象低端保市场" class="newsimg" lang="http://img2.cache.netease.com/stock/2015/8/26/20150826114130e63d4_550.jpg"><img src="http://s.cimg.163.com/stock/2015/8/26/20150826114130e63d4_550.jpg.119x83.jpg" alt="国产手机端保形象低端保市场" /></a>                                <p>[摘要：低端机型的狂暴、高端机型的低迷，成为目前国产手机品牌高速发展历程中的畸形态势。如果按照正常情况，应该是同步发展，二者之间的销量等不会过大，都有固定的消费群体。而不是现在这样，高端机型的消费群体主动将注意力转向低端机型市场。]原标题：[亦观察] No.612&nbsp;  ...<br />
#                   <span class="time">2015-08-26 11:45:14</span>
 
 
def getCoder(url):
    html = urllib.urlopen(url)
    print html.info()
    page = html.read()
#    rule = r'<a href="(.+?)"title="(.+?)"'    #class="newsimg"'  # class="time">(.+?)<'
    rule2 = 'class="time">(.+?)<\/span>'
    rule = '<h2><a href="(.+?)">(.+?)<\/a><\/h2>'
    
    pat = re.compile(rule)
    pat2 = re.compile(rule2)

    coderList = re.findall(pat, page)
    coderList2 = re.findall(pat2, page)
    html.close()
    
#    print isinstance(str(coderList[0]), unicode)
    
#    print type(coderList[0])

#    print coderList[0][1].decode('GBK').encode('utf-8')

    print len(coderList)
    print len(coderList2)

    for i in xrange(len(coderList)):
        print coderList[i][1].decode('GBK').encode('utf-8')
        print coderList[i][0]
       
#getCoder(url)





'''
作业2：

url: "http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter"


print jd_search(keyword)

[dict,dict,dict]
dict {pic:'',title:'',price:'',url:''}

'''

url = "http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter"

def get_goods(url):
    html = urllib.urlopen(url)
    content = html.read()
    soup = BeautifulSoup(content)
    html.close()
    print soup.title
    print soup.title.name
    print soup.title.string
    print soup.p
    print soup.find(id = 'plist')
    print soup.get_text()
#    print soup.findAll('a')
get_goods(url)

'''可以看出：soup 就是BeautifulSoup处理格式化后的字符串，soup.title 得到的是title标签，soup.p  
得到的是文档中的第一个p标签，要想得到所有标签，得用find_all

函数。find_all 函数返回的是一个序列，可以对它进行循环，依次得到想到的东西.

get_text() 是返回文本,这个对每一个BeautifulSoup处理后的对象得到的标签都是生效的。
你可以试试 print soup.p.get_text()

如何遍历树？

　使用find_all 函数

find_all(name, attrs, recursive, text, limit, **kwargs)

举例说明：

print soup.find_all('title')
print soup.find_all('p','title')
print soup.find_all('a')
print soup.find_all(id="link2")
print soup.find_all(id=True)

'''