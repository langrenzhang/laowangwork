#coding=utf-8
import xlrd
from pyExcelerator import *

#打开要写入的源txt文件
with open('log.txt', 'r') as f:
    a = f.readlines()
    
#下面是写和处理数据
w = Workbook()                            #创建一个工作簿
ws = w.add_sheet('Hi, gao ting ting')     #创建一个工作表
for i in xrange(len(a)):                       #将数据写入工作表
    ws.write(i,0,a[i])
w.save('txt_to_xls10.29.xls')     #保存

