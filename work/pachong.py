#coding=utf-8

"""
pythoner:张硕
source : iplaypython.com
"""

import urllib

#print dir(urllib)          #列出方法

#print help(urllib.urlopen) #POST/GET  proxies 代理

url = "http://www.iplaypython.com"
#url = "http://www.163.com"

html = urllib.urlopen(url)

#print dir(html)              #列出方法

#print html.read().decode("gbk").encode("utf-8")   #不同编码的转换

#print html.info()             #爬出header头部信息

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

#print html.geturl()  #返回传入的url

#urllib.urlretrieve(url, "/home/zhangshuo/163.txt")     #将网页保存本地 或者用open来打开保存











html.close()    #关闭打开的文件

