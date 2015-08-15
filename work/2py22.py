#coding=utf-8
import time
import threading
import urllib
'''
first test 
'''

def test1(p):
    time.sleep(1.001)
    print p
info = [2,5,6,9,25,888]
ts = []
for i in info:
    th = threading.Thread(target=test1,args=[i])
    ts.append(th)
    th.start()

for i in ts:
    i.join()
print "The end"

print "**************************************************"

'''
second test
'''

def test2(p):



url_info = ['www.baidu.com','www.sina.com','www.qq.com']
