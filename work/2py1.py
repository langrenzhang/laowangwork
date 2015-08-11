#coding=utf-8
import os
import glob
import urllib

def judge_int(*kr):   
    a = list(kr)   
    a.sort()
    print "The max is {max},min is {min}".format(max = a[-1], min = a[0])
     
def judge_long_str(*kr):
    d = {}
    for i in kr:
        d[i] = len(i)
    dict = sorted(d.iteritems(), key=lambda d1: d1[1])     
    print max(d, key=d.get)
#    print min(d, key=d.get)
    
def get_doc(module):
    a = 'pydoc %s'%module
    m = os.popen(a).read()
    return m

def get_text(f):
    a = 'cat %s'%f
    m = os.popen(a).read()
    print m

def get_item(f):
    a = "%s/*.*"%f
    if os.path.exists(a):
        print "The files is exist"
    tmp = glob.glob(a)
    if tmp == []:
        print "The file is empty"
    else:
        print tmp[2]
        print len(tmp) 
        print type(tmp)
        for i in xrange(len(tmp)): print tmp[i]
        
def get_num(*g):
    a = []
    for i in g:
        if isinstance(i, int):
            if i%2==0:
                a.append(i)
        else:
            print "type is error ;the wrong is:%s"%i            
    print a

 
def get_page(u):
        
#    a = urllib.urlopen(u).read()
#    print a  
   
    baidu = urllib.urlopen(u)  
    print type(baidu.read())
    print '#################http header:', baidu.info()  
    print '###################http status:', baidu.getcode()  
    print '#################url:', baidu.geturl()  
    print baidu.read()
    for line in baidu: # 就像在操作本地文件  
        print "###########"
        print line,
    baidu.close()  
    
   
        
x,y,z,a,b,c,d = 3,5,2,5,7,44,432
judge_int(x,y,z,a,b,c,d)


a = '123456'
b = 'zhangshuo'
c = 'woshihaoren'
judge_long_str(a,b,c)


a = "urllib"
print type(get_doc(a))
print dir(get_doc.__code__)

#a = 'a.txt'
#get_text(a)


#a = '/home/zhangshuo/worksapce'
#b = '/bi'
#get_item(a)

get_num(1,2,3,4,5,6,952,a,b)
#a = "https://www.baidu.com/"
#get_page(a)

