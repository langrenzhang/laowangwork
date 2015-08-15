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
pirnt t2-t1

print "**********************************************"

yield:

'''
def fbs(fs):
    x,y = 1,1
    f = [x]
    while fs>y:
        f.append(y)
        x,y = y,x+y
    return f
print fbs(10) 
a = 2      
b = 3
print a
print b
a,b = b,a
print a,b

















  







