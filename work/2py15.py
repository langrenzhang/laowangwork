#!/usr/bin/env python
#coding=utf-8
import os
import string 
import urllib
import logging   

'''
1 定义一个函数func(filename) filename:文件的路径，函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误。

'''
def fun1(filename):
    try:
        file_path = open(filename, 'r')       
    except:
        print filename, "is not found"
    else:
        content = file_path.read()
        print content
        file_path.close()
#    finally:
#        d.close()
        
#filename = '/home/zhangshuo/worksapce/a.txt'
#filename = '/zhangshuo'
#fun1(filename)

'''
定义一个函数func(urllist)   urllist:为URL的列表，例如：['http://xx.com','http://www.xx.com','http://www.xxx.com'...] 

函数功能：要求依次打开url，打印url对应的内容，如果有的url打不开，则把url记录到日志文件里，并且跳过继续访问下个url。

'''

def fun2(urllist):
    for i in urllist:
        try:
            d = urllib.urlopen(i)
            content = d.read()
            save_d = open('/home/zhangshuo/worksapce/save.txt', 'a+')
            content = "".join([content,"******************"])
            save_d.write(content)
            save_d.close()            
            d.close()
        except:
            error_d = open('/home/zhangshuo/worksapce/log.txt', 'a+')
            i = "".join([i,"********"])
            error_d.write(i)
            error_d.close()
  
urllist = ['abcdefg','www.www   ','http://svgporn.com/']
  
#fun2(urllist)
  
  
  
#
#logger = logging.getLogger()
#logfile = 'test.log'
#hdlr = logging.FileHandler('/tmp/sendlog.txt')
#formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
#hdlr.setFormatter(formatter)
#logger.addHandler(hdlr)
#logger.setLevel(logging.NOTSET)


#print logger.debug('this is debug message')
#print logging.basicConfig(level=logging.INFO)
logging.debug('debug message')  
logging.info('info message')  
logging.warning('warning message')  
logging.error('error message')  
logging.critical('critical message')    




logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',filename='/tmp/test.log',filemode='w')  
logging.debug('debug message')  
logging.info('base info message')  
logging.warning('base warning message')  
logging.error('base error message')  
logging.critical('base critical message')  















'''

3 定义一个函数func(domainlist)   domainlist:为域名列表，
例如：['xx.com','www.xx.com','www.xxx.com'...]
函数功能：要求依次ping 域名，如果ping 域名返回结果为：request time out，
则把域名记录到日志文件里，并且跳过继续ping下个域名。（提示用os模块的相关方法）

'''

#def fun3(urllist):
    
#a = "ping -c 1 "
#b = "www.sina.com"
#b = "127.0.0.259"
#c = "".join([a,b])
#d = os.popen(c).read()



#logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.DEBUG)  
#logging.debug('this is a message') 