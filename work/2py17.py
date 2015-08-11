#!/usr/bin/env python
#coding=utf-8
import os
import logging   

logger = logging.getLogger()
#logfile = 'test.log'
hdlr = logging.FileHandler('/tmp/sendlog.txt')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.NOTSET)


logger.debug('this is debug message')

'''
定义一个函数func(filename) filename:为文件名，用with实现打开文件，并且输出文件内容
'''

def func1(filename):
    with open(filename) as a:
        print a.read()
        
#func1('/home/zhangshuo/worksapce/a.txt')

'''
定好一个函数func(listinfo) listinfo:为列表，listinfo=[133,88,33,22,44,11,44,55,33,22,11,11,444,66,555] 
返回一个列表包含小于100的偶数，并且用assert来断言返回结果和类型

'''
def fun2(listinfo):
    res_list = filter(lambda x:x%2==0, listinfo)
    res_list = filter(lambda x:x<100 , res_list)
    assert type(res_list) == list
    print res_list

listinfo=[133,88,33,22,44,11,44,55,33,22,11,11,444,66,555]
#fun2(listinfo)

'''
自己定义一个异常类，继承Exception类, 捕获下面的过程：
判断raw_input()输入的字符串长度是否小于5，如果小于5，
比如输入长度为3则输出:" The input is of length 3,expecting at least 5'，
大于5输出"print success'

'''

