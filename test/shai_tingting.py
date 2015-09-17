#coding=utf-8
#
#with open('phone1.txt', 'r') as fil1:
#    a = fil1.readlines()
import xlrd
from pyExcelerator import *

#下面是读和处理数据
data = xlrd.open_workbook('21.xls')
table = data.sheets()[0]          #通过索引顺序获取
#a = table.row_values(1)
a = table.col_values(1)
#a = list(set(a))
b = table.col_values(2)
#b = list(set(b))
#print len(a)
#print len(b)
a.extend(b)
#print len(a)
a = list(set(a))
l = len(a)
#print type(a)
#print a[-1]

#下面是写和处理数据
w = Workbook()     #创建一个工作簿
ws = w.add_sheet('Hi, gao ting ting')     #创建一个工作表


for i in xrange(l):
    ws.write(i,0,a[i])

#ws.write(0,0,'bit')    #在1行1列写入bit
#ws.write(0,1,'huang')  #在1行2列写入huang
#ws.write(1,0,'xuan')   #在2行1列写入xuan
w.save('ting.xls')     #保存