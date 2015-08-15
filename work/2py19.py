#coding=utf-8
import threading
import time
import re
import urllib
'''
多线程

进程 pid 唯一标示符
使用kill 杀死进程

主线程 创造一个进程的时候，会创造一个线程，这个线程被称为主线程
一个进程里只有一个主线程

python里的多线程，不是真正意义上的多线程。

全局锁

在任意的指定时间里，有且只有一个线程在运行

a b c
'''

#
#def test(p):
##	time.sleep(0.001)
#	print p
#ts = []
#for i in xrange(0,15):
#	th = threading.Thread(target=test, args=[i])
#	th.start()
#	ts.append(th)
#
#for i in ts:
#	i.join()
#
#print "hoho,end!!!!!"
#print type(ts)
#
#print ts



'''
习题：
习题一：已知列表 info = [1,2,3,4,55,233]

生成6个线程对象,每次线程输出一个值，最后输出："the end"。

'''

#
#def test1(i):
#	print i
#
#ts = []	
#info = [1,2,3,4,55,233]
#for i in info:
#	th = threading.Thread(target=test1, args=[i])
#	th.start()
#	ts.append(th)
#	
#for i in ts:
#	i.join()
#	
#print "the end"
#		

'''
习题二：已知列表 urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com'] 
用多线程的方式分别打开列表里的URL，并且输出对应的网页标题和内容。
'''


ts = []
urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com'] 

def git_url(url):
    u = urllib.urlopen(url).open()
    re_title = '<title>(.*)</title>'  #</head>
    title = re.findall(re_title.u)
    print title[0],u

# xian cheng queue--dueilie   //yield

for i in urlinfo:
    th = threading.Thread(target = git_url,args = [i])
    th.start()
    ts.append(th)


for i in ts:
    i.join()








'''
习题三：已知列表 urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com']
 用多线程的方式分别打开列表里的URL，输出网页的http状态码。

'''


		
