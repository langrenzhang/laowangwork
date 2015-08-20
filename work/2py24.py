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
###################################################################
## 将正则表达式编译成Pattern对象
#pattern = re.compile(r'hello')
# 
## 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
#match = pattern.match('hello world')
# 
#if match:
#    # 使用Match获得分组信息
#    print match.group()
# 
#### 输出 ###
## hello

#m = re.match(r'hello', 'hello world!')
#print m.group()
#print dir(m )

#1
info = '<a href="http://www.baidu.com">baidu</a>'
#print info
pattern1 = re.compile(r'"(.*?)"')
#print pattern1
match1 = pattern1.findall(info)
print match1

#2
pattern2 = re.compile(r'>(.*?)</a>')
#print pattern2
match2 = pattern2.findall(info)
print match2

print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

content = "one1two2three3four4"
pattern3 = re.compile(r'\d')
match3 = pattern3.findall(content)
print match3
#print re.split(r'\d',content)



print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#3查找所有包含'oo'的单词
text = "JGood is a handsome boy, he is cool, clever, and so on..." 

con_oo = re.split(r'\s',text)
#print con_oo
for i in con_oo:
    if "oo" in i:
        print i

'''
已知字符串：

info = 'test,&nbsp;url("http://www.baidu.com")&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'

要求完成下面2个小功能：
1.1 关闭[img]标签
1.2 将url()中的["]转为[']

最后结果字符串：

"test,&nbsp;url('http://www.baidu.com')&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com"></img>ininnnin<img src="http://www.dd.com"></img>"

'''

print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#1.1 关闭[img]标签
info = 'test,&nbsp;url("http://www.baidu.com")&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'
#print info
#print type(info)
pattern4 = re.compile(r'<img(.*?)>')
match4 = pattern4.findall(info)
#print match4
for i in match4:
#    print "!!!!!!!!!!!!"
    a = "".join(['<img',i])
    b = "".join([a,'>'])
#    print b
#    print b in info
    info = info.replace(b,' ')
    
print info
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#1.2 将url()中的["]转为[']

pattern5 = re.compile(r'url\((.*?)\)')
match5 = pattern5.findall(info)
#print type(match5)
tihuan = match5[0].replace('"','\'')
print info.replace(match5[0],tihuan)
