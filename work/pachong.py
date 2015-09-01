#coding=utf-8
#! /usr/bin/python
"""
pythoner:张硕
source : iplaypython.com
"""

import urllib
import chardet   #字符集检测

#print dir(urllib)          #列出方法

#print help(urllib.urlopen) #POST/GET  proxies 代理

#url = "http://www.iplaypython.com"
#url = "http://www.163.com"
#url = "http://www.youku.com"
#url = "http://www.dangdang.com"
#url = "http://www.sina.com"
url = "http://www.jd.com"
#url = "http://www.baidu.com"
#url = "http://www.gccaifu.com/admin.php"

urls = ["http://www.iplaypython.com",
        "http://www.163.com",
        "http://www.youku.com",
        "http://www.dangdang.com",
        "http://www.sina.com"       
        ]






html = urllib.urlopen(url)

#print dir(html)              #列出方法

#print html.read().decode("gbk","ignore").encode("utf-8") #不同编码的转换，先将gbk转换为unicode，再换为utf-8

#info = html.info()             #爬出header头部信息

#print info

#print dir(info)                #info的一些方法

#print info.getparam('charset')

"""
返回状态码
200正常访问
301重定向
404网页不存在
403禁止访问
500状态

HTTP 权威指南，纸质版。 
"""
#print html.getcode()      

#code = html.getcode()
#print code

#print type(code)

#if code == 200:
#    print html.info()
#else:
#    print "404"

#print html.geturl()  #返回传入的url

local = "/home/zhangshuo/163.txt"

"""
url.urlretrieve 有三个参数
1 传入网址，网址的类型一定是字符串
2 传入的地址，本地网页的保存路径——绝对路径和文件名
3 一个函数的调用，我们可以任意来定义这个函数的行为，
但是一定要保证这个函数有三个参数
  1）到目前为此传递的数据块数量
  2）是每个数据块的大小，单位是byte，字节
  3）远程文件的大小。（有时候返回-1）

  @a:是XXXXXXXX
  @b:是XXXXXXXX
  @c:是XXXXXXXX  
"""
#显示下载进度
def callback(a,b,c):
    download_progress = 100.0*a*b/c	
    if download_progress > 100:
        download_progress = 100        
    print "%.2f%%"%download_progress
    
def callback_test(*a):
    """
    1）到目前为此传递的数据块数量
    2）是每个数据块的大小，单位是byte，字节
    3）远程文件的大小。（有时候返回-1）    
    """
    print a
#urllib.urlretrieve(url, local, callback_test)     #将网页保存本地 或者用open来打开保存

content = html.read()
#print content

#print chardet.detect(content)   #返回一个字典检测编码格式：可信度  百分比 ，编码  

def automatic_detect(url):
    
    """
    检测网址的编码格式的封装
    """
    content = urllib.urlopen(url).read()
    result = chardet.detect(content)
    encoding = result['encoding']
    return encoding

#print automatic_detect(url)
for i in urls:
    j = automatic_detect(i)
    print ":".join([i,j])

html.close()    #关闭打开的文件

