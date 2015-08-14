#coding=utf-8
import threading
import time

'''
num = 0 
def t():
    global num 
    num +=1
    print num 
ds = []
for i in xrange(0,10):
    d = threading.Thread(target=t)
    d.start()
    ds.append(d)

for i in ds:
    i.join()

print 'hello world'   
print '*****************************************'
def a():
   
    print 'a begin'
    time.sleep(2)
    print 'a end'

def b():
    print 'b begin'
    time.sleep(2)
    print 'b end'

t1 = time.time() 

print t1
a() 
b()
print time.time() - t1

print '*****************************************'
t1 = time.time()
sa = threading.Thread(target=a)
sb = threading.Thread(target=b)
sa.start()
sb.start()
sa.join()
sb.join()

t2 = time.time()

print t2 - t1

print '****************************************'

mlock = threading.RLock()

print num


def l():
    global num
    mlock.acquire()     #plus lock
    num = num + 1
    print num           #do some code
    mlock.release()     #unlock

for i in xrange(0,15):
    d = threading.Thread(target=l)
    d.start()
print '***************************************'

total = 500
mlock = threading.Rlock()
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
pirnt t2-t1

print "**********************************************"

yield:

'''
f = [1,1]
def fbs(fb):
    s1 = 1
    s2 = 1
    s3 = 2
    while fb>s3:
#        fb-=1
        s3 = s1 + s2
#        print s3
        f.append(s3)
        s1 = s2
        s2 = s3
    f.pop()       

fbs(100) 
print f
        


















  







