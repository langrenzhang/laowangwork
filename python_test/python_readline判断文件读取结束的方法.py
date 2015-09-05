#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
本文实例讲述了python中readline判断文件读取结束的方法。分享给大家供大家参考。具体分析如下：

大家知道，python中按行读取文件可以使用readline函数，下面现介绍一个按行遍历读取文件的方法，通过这个方法，展开我们要讨论的问题：

我在代码中写的if(aLine != '' ):部分。当readline读取到为空的时候，意味着读到了文件的结束。这个时候，问题就在这里，很多人会想，是不是遇到一个空行，也会被认为是文件的结束呢？这就引入了标题的问题。

事实上，文件的空白行并不会返回一个空行。因为在每一行的末尾还有一个或者多个分隔符，因此“空白行”至少会有一个换行符或者系统使用的其他符号。所以，即使文件中真的包含一个“空白行”，读入的行也不是空的，这就意味着在真实遍历读取到文件结束之前，程序实际上是不会停止的

readline() 和 .readlines() 非常相似。它们都在类似于以下的结构中使用：
Python .readlines()
'''
#第一种方式
filename = raw_input('Enter your file name')  #输入要遍历读取的文件路径及文件名
file = open(filename,'r')
done = 0
while not  done:
        aLine = file.readline()
        if(aLine != ''):
            print aLine,
        else:
            done = 1
file.close()   #关闭文件
#第二种方式  

'''
.readline() 和 .readlines() 之间的差异是后者一次读取整个文件，象 .read() 一样。.readlines() 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理。另一方面，.readline() 每次只读取一行，通常比 .readlines() 慢得多。仅当没有足够内存可以一次读取整个文件时，才应该使用 .readline()。

readlines返回行数问题

官方文档这样写的：
If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.

确实是指定大小啊并且会受内部缓冲区大小影响向上取整到内部缓冲区大小。内部缓冲区大约是8k也难怪我每次测试文件大小都是8k（8192）倍数
'''
fh = open('c:\autoexec.bat')
for l in  fh.readlines(): print  l 
fh.close()