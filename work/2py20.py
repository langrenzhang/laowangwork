#coding=utf-8
import threading
import time
import urllib

'''
1.全局锁（GIL）是一个很重要的概念。

在任意一个指定的时间，有且只有一个线程在运行 -》 python是线程安全的

线程安全 歧义


2.多线程 复杂度高，不建议使用。（它用在哪里？）

一个程序的复杂度，大部分情况下，只和代码行数有关。
简单 ！= 简陋

数据库连接池

3.多线程还是有点爽的，比如？

4.io操作用到多线程？必须要lock，acquire release
互斥锁

加锁 acquire
释放锁 release
加锁 一定 释放
死锁 

5.rlock 可重入锁



# import threading

# num = 0
# def t():
# 	global num
# 	num += 1
# 	print num

# for i in xrange(0,10):
# 	d = threading.Thread(target=t)
# 	d.start()

import time

def a():
print 'a begin'
time.sleep(2)
print 'a end'

def b():
print 'b begin'
time.sleep(2)
print 'b end'

# b_time = time.time()
# a()
# b()
# print time.time() - b_time #代码完成时间


# import threading


# b_time = time.time()

# _a = threading.Thread(target=a)
# _b = threading.Thread(target=b)
# _a.start()
# _b.start()

# _a.join()
# _b.join()

# print time.time() - b_time #代码完成时间


import threading

mlock = threading.RLock()

num = 0
def a():
global num

mlock.acquire() #加锁
num += 1 #你要执行的代码
mlock.release() #释放锁

print num

for i in xrange(0,10):
d = threading.Thread(target=a)
d.start()



习题：

有10个刷卡机，代表建立10个线程，每个刷卡机每次扣除用户一块钱进入总账中，每个刷卡机每天一共被刷100次。账户原有500块。所以当天最后的总账应该为1500

用多线程的方式来解决，提示需要用到这节课的内容


'''



total = 500
mlock = threading.RLock()
def test():
    global total
    mlock.acquire()

    for i in xrange(0,100):
        
        total = total + 1

    mlock.release()

t1 = time.time()
st = []
for i in xrange(0,10):
    sh = threading.Thread(target=test)    
    sh.start()
    st.append(sh)
    print total

for i in st:
    i.join()
t2 = time.time()
print t2-t1
