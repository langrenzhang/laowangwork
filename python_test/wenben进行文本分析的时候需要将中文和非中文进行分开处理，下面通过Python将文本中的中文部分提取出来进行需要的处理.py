#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import re                                                        #导入正则表达式模块：re模块

def translate(inputFile, outputFile):
	fin = open(inputFile, 'r')                                   #以读的方式打开输入文件
	fout = open(outputFile, 'w')                                 #以写的方式打开输出文件

	for eachLine in fin:                                         #按行读入文件内容
		line = eachLine.strip().decode('utf-8', 'ignore')        #处理前进行相关的处理，包括转换成Unicode等
		
		p2 = re.compile(ur'[^\u4e00-\u9fa5]')                    #中文的编码范围是：\u4e00到\u9fa5
		
		zh = " ".join(p2.split(line)).strip()                    
		zh = ",".join(zh.split())

		outStr = zh                                              #经过相关处理后得到中文的文本

		fout.write(outStr.strip().encode('utf-8') + '\n')
		
	fin.close()
	fout.close()

if __name__ == '__main__':
	translate(sys.argv[1], sys.argv[2])                          ##通过获得命令行参数获得输入输出文件名来执行，方便

