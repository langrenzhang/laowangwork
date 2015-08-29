#coding=utf-8
import threading
import time
import re
import urllib
import socket

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
def caturl(url):
  
    u_file = urllib.urlopen(url).read()
#    print type(u_file)
#    print u_file


#    with open('/home/zhangshuo/url.txt','w') as a:
#        a.write(u_file)


    parttent = re.compile(r'<div class="list_item clearfix">(.*?)<div class="item_bottom">')
    match = parttent.findall(u_file)
    return match
   
url = "http://money.163.com/special/pinglun/"
print caturl(url)
    


'''
作业2：

url: "http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter"


print jd_search(keyword)

[dict,dict,dict]
dict {pic:'',title:'',price:'',url:''}

'''
d

