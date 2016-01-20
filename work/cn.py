# -*- coding: utf-8 -*-

import sys

"""
python 内部是Unicode.格式编码

中文是gbk

正常的话是utf-8

乱码 -> unicode中转码 -> 我们需要的编码格式

decode() -> unicode -> encode() 转换我们需要的编码

demo:content.decode('gbk').encode('utf-8')
先解码到unicode在编码到utf-8（万国码） 完成我们要的格式

if isinstance(content, unicode):
    print "is unicode."
elif isinstance(content, gbk):
    print  "is gbk"
else:
    print "not gbk and unicode"
"""

#显示当前编码格式
print sys.getdefaultencoding()

with open('/home/zhangshuo/me.txt', 'r') as me:
    content = me.read()

if isinstance(content, unicode):
    print "is unicode."
#elif isinstance(content, gbk):
#    print  "is gbk "              #这个有问题gbk好像不是内置的常量      
else:
    print "not gbk and unicode"
print content