#coding=utf-8
#! /usr/bin/python
"""
pythoner:张硕
source : iplaypython.com
"""

"""
test 
#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#Filename:urllib2-header.py
 
import urllib2
import sys
 
#抓取网页内容-发送报头-1
url= "http://www.phpno.com"
send_headers = {
    'Host':'www.phpno.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection':'keep-alive'
}
 
req = urllib2.Request(url,headers=send_headers)
r  = urllib2.urlopen(req)
 
html = r.read()                             #返回网页内容
receive_header = r.info()                   #返回的报头信息
 
# sys.getfilesystemencoding() 
html = html.decode('utf-8','replace').encode(sys.getfilesystemencoding())   #转码:避免输出出现乱码 
 
print receive_header
# print '####################################'
print html
#该代码片段来自于: http://www.sharejs.com/codes/python/5716


"""
import urllib2
import urllib

#url = "http://blog.csdn.net/raylee2007/article/details/48163715"
url = "http://blog.csdn.net/raylee2007"

html = urllib.urlopen(url)

content = html.read()

#print html.getcode()    

print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

#html2 = urllib2.urlopen(url)

#print html2.read()

#header头的信息传递   有问题
my_headers = {
    "Host": "blog.csdn.net",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Connetion": "keep-alive"    
    }
        
#req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0")
#req.add_header("GET",url)
#req.add_header("Host", "blog.csdn.net")
#req.add_header("Referer", "http://blog.csdn.net/raylee2007")

req = urllib2.Request(url, headers = my_headers)

content = urllib2.urlopen(req)
html = content.read()  
receive_header = content.info()

print receive_header
#print html

