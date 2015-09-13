#coding=utf-8
#import threading
#import time
#import re
import urllib
from bs4 import BeautifulSoup
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
#弄完了，哈哈哈哈哈哈哈哈高兴呀
def get_dict(url):
    html = urllib.urlopen(url)
    content = html.read()
    html.close()
    soup = BeautifulSoup(content)
    con = soup.find_all('a', class_ = 'newsimg')
    print con[0].get('href')
    print con[0].get('title')
    print soup.find_all('span', class_ = 'time')[0].get_text()

#url = "http://money.163.com/special/pinglun/"
#get_dict(url)

#for con in soup.find_all('a', class_ = 'newsimg'):
#    print con
'''
作业4：

使用scrapy完成作业2的需求。

jd_search(keyword,page_skip=1,page_limit=10) #抓1后面10页（包括第10页）的内容。
jd_search(keyword,page_skip=4,page_limit=3) #抓4后面3页（包括第6页）的内容。

'''


url = "http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter"

def get_goods(url):
    html = urllib.urlopen(url)
    content = html.read()
    html.close()
    
