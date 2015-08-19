#coding=utf-8
import threading
import time
import re
import urllib


'''
1 已知字符串:
info = '<a href="http://www.baidu.com">baidu</a>'

用正则模块提取出网址："http://www.baidu.com"和链接文本:"baidu"

2 字符串："one1two2three3four4" 用正则处理，输出 "1234"

3 已知字符串：text = "JGood is a handsome boy, he is cool, clever, and so on..." 查找所有包含'oo'的单词。

'''
info = '<a href="http://www.baidu.com">baidu</a>'

s = re.split('\"\"',info)
print s








'''
已知字符串：

info = 'test,&nbsp;url("http://www.baidu.com")&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'

要求完成下面2个小功能：
1.1 关闭[img]标签
1.2 将url()中的["]转为[']

最后结果字符串：

"test,&nbsp;url('http://www.baidu.com')&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com"></img>ininnnin<img src="http://www.dd.com"></img>"

'''
