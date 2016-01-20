#coding=utf-8
'''

'''
import xlrd
from pyExcelerator import *

#下面是读和处理数据
data = xlrd.open_workbook('10.2.xls')
table = data.sheets()[0]          #通过索引顺序获取第一个工作表
#a = table.row_values(1)
a = table.col_values(1)           #获取列
a = list(set(a))                  #去重
print type(a)                 
print len(a)

#a2 = table.col_values(1)
#a2 = list(set(a2))
#print len(a2)
#a3 = table.col_values(2)
#a3 = list(set(a3))
#print len(a3)
#a4 = table.col_values(3)
#a4 = list(set(a4))
#print len(a4)
#a5 = table.col_values(4)
#a5 = list(set(a5))
#print len(a5)
#a.extend(a2)
#a.extend(a3)
#a.extend(a4)
#a.extend(a5)
#a = list(set(a))
#print len(a)



b = table.col_values(3)
#b2 = table.col_values(6)
#b.extend(b2)
b = list(set(b))
print type(b)
print len(b)
#print len(a)
#print len(b)
for i in b:
    if i in a:
        a.remove(i)

print len(a)
#a.extend(b)
#print len(a)
#a = list(set(a))

#l = len(a)
#print l

#print type(a)
#print a[-1]



#下面是写和处理数据

w = Workbook()                            #创建一个工作簿
ws = w.add_sheet('Hi, gao ting ting')     #创建一个工作表
for i in xrange(len(a)):                       #将数据写入工作表
    ws.write(i,0,a[i])
    
#ws.write(0,0,'bit')    #在1行1列写入bit
#ws.write(0,1,'huang')  #在1行2列写入huang
#ws.write(1,0,'xuan')   #在2行1列写入xuan
w.save('ting10.12.xls')     #保存
