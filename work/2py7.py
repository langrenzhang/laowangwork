#coding=utf-8
import os
import glob
import urllib
import string

class test():
    def get(self,b):
#        print self
        return b    
a = test()
b = "zhangshuo"
print a.get(b)
'''
定义一个学生类。有下面的类属性：

1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]

类方法：

1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
'''

class student():
    def __init__(self,name,age,score):
        self.name =name
        self.age = age
        self.score = score
    
    def get_name(self):
        if isinstance(self.name,str):
            return name
        else:
            return "type name is error"
    def get_age(self):
        if isinstance(self.age,int):
            return age
        else:
            return "type age is error"
    def get_score(self):
        a = self.score.values()
        b = sorted(a)
        print b[-1]
        if isinstance(self.score,dict):
            return max(self.score,key=self.score.get)
        else:
            return "the type dict is error"
        
    
    
name = "zhangshuo"
age = 29
score = {"Chinese":99,"Math":100,"English":150}
zhang = student(name,age,score)

print zhang.get_name()
print zhang.get_age()
print zhang.get_score()

#zm = student('zhangming',20,[69,88,100])
#print zm.get_name()
#print zm.get_age()
#print zm.get_score()
#lq = student('liqiang',23,[82,60,99])
#print lq.get_name()
#print lq.get_age()
#print lq.get_score()

class dictclass():
    def __init__(self,obj_dic):
        self.obj_dic = obj_dic
    def del_key(self,key):
        del self.obj_dic[key]
        return self.obj_dic
    def key_indict(self,key):
        if self.obj_dic.haskey(key):
            return "in it"
        else:
            return "not found"
    def get_key(self):
        return self.obj_dic.keys()
    
#obj_dic = {"Chinese":99,"Math":100,"English":150}
#dic = dictclass(score)
#print dic.get_key()
#print dic.key_indict("English")


'''
定义一个列表的操作类：Listinfo

包括的方法: 

1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key() 

list_info = Listinfo([44,222,111,333,454,'sss','333'])

'''


class Listinfo():
    def __init__(self,ls):
        self.ls = ls
        
    def print_list(self):
        return self.ls
                
    def add_key(self,keyname):
        if isinstance(keyname,int) or isinstance(keyname,str):
            self.ls.append(keyname)
            return self.ls
        return "type is error"
    def get_key(self,num):
        if isinstance(num,int):
            return self.ls[num]
        return "type is error"
    def update_list(self,lis):
        if isinstance(lis,list):
            self.ls.extend(lis)
            return self.ls
        return "type is error"
    def del_key(self):
        return self.ls.pop()
    def ls_ty(self):
        return type(self.ls)
    
list_info = Listinfo([44,222,111,333,454,'sss','333'])
list_info.add_key(name)
print list_info.print_list()
print list_info.ls_ty()
print list_info.get_key(3)
print list_info.print_list()
list_info.update_list([1,2,4,5,6,'a','b','d'])
print list_info.print_list()
print list_info.del_key()
print list_info.print_list()

   
