#coding=utf-8

"""
pythoner:张硕
source : iplaypython.com
"""

import urllib

#print dir(urllib)          #列出方法

#print help(urllib.urlopen) #POST/GET  proxies 代理

#url = "http://www.iplaypython.com"
url = "http://www.163.com"
#url = "http://www.gccaifu.com/admin.php"

html = urllib.urlopen(url)

#print dir(html)              #列出方法

#print html.read().decode("gbk","ignore").encode("utf-8") #不同编码的转换，先将gbk转换为unicode，再换为utf-8

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

code = html.getcode()

#print code
#
#print type(code)

if code == 200:
    print html.info()
else:
    print "404"

#print html.geturl()  #返回传入的url

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
def calllback(a,b,c):
    down_progress = 100.0*a*b/c	
    if download_progress > 100:
        download_progress = 100        
    print "%.2f%%"%down_progress,
urllib.urlretrieve(url, "/home/zhangshuo/163.txt",calllback)     #将网页保存本地 或者用open来打开保存











html.close()    #关闭打开的文件

