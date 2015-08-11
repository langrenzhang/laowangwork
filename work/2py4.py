#coding=utf-8
import os
import glob
import urllib
import string
def f_doc(a):
    '''
    this file was a best thing in the world
    '''
    pass

 
#定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，
#如果该函数没有描述文档，则返回"not found"
def get_fundoc(func = None):
    if func==None:
        print "not found"
    else:
        print func.__doc__
get_fundoc(f_doc)

#定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型
def get_cjsun(a):
    print range(a)[1:]
    return reduce((lambda x,y:x*x+y*y), range(a)[1:])    
a = 8
print get_cjsun(a)

#定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行
#一些相关的操作，不会影响到原来列表的元素值
def list_info(a):
    b = a 
    c = sorted(b)
    return c 
a =[1,5,687,6]
print list_info(a)
print a

#定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，
#如果可以调用则返回该函数名(类型为str)，否则返回 “fun is not function"
def get_funcname(func):
    if callable(func):
        return func.__name__
    else:
        return "fun is not function"
    
print get_funcname(list_info)
#python __code__用法
print dir(f_doc.__code__)
print f_doc.__code__.co_filename
print f_doc.__code__.co_name

#函数参数的使用

#位置匹配 func(name)
def get_par1(a,b,c):
    print a
    print b
    print c
#关键字匹配 func(key=value)
def get_par2(a=None,b="zhong guo",c=''):
    print a
    print b
    print c
#* kargs 元组
def get_par3(*kargs):
    print kargs    
#** kwargs 字典
def get_par4(**kwargs):
    print kwargs  


get_par1(10,2,3)
get_par2(c=10,a=[1,2,3])
get_par3(1,2,3,4)
get_par4(a=1,b=2,c=3)


#用lambda和filter完成下面功能：输出一个列表，列表里面包括：1-100内的所有偶数。
#（提示：可以用filter,lambda）
a = filter(lambda x:x%2==0,range(101)[1:])
print a 

#传递3个列表参数：
#[1,2,3],[1,5,65],[33,445,22]
#返回这3个列表中元素最大的那个，结果是：445
def max_list(*args):
    a = None
    for i in range(len(args)):
        for j in range(len(args[i])):
            a = max(a,args[i][j])
    return a
a = [1,2,3]
b = [1,5,65]
c = [33,445,22]
print max_list(a,b,c)

#定义一个func(name)，该函数效果如下(传入str首字母大写)
def cap_func(a):
    b = a[0].upper()
    c = "".join([b,a[1:]])
    return c
a = "lilei"
b = "hello world"
print cap_func(b)
assert cap_func(a) == "Lilei"
assert cap_func("hanmeimei") == "Hanmeimei"
assert cap_func("Hanmeimei") == "Hanmeimei"

#定义一个func(name,callback=None),效果如下。         利用了string这个包
#assert func("lilei") == "Lilei"
#assert func("LILEI",callback=string.lower) == "lilei"
#assert func("lilei",callback=string.upper) == "LILEI"
def change_size_func(name,callback=None):
    if callback==None:
        return name.capitalize()
    else:
        return callback(name)
        
print change_size_func("lilei")
print change_size_func("hello world",callback=string.upper)
assert change_size_func("lilei") == "Lilei"
assert change_size_func("LILEI",callback=string.lower) == "lilei"
assert change_size_func("lilei",callback=string.upper) == "LILEI"

#定义一个func(*kargs)，该函数效果如下。
#assert func(222,1111,'xixi','hahahah') == "xixi"
#assert func(7,'name','dasere') == 'name'
#assert func(1,2,3,4) == None
# fans tips excampls

def short_str(*kargs):
    '''
    shortstr(*kargs) -> str or None
    return the shortest str in the kargs, or return None if no str in it.
    '''
    #过滤非字符串
    lis = filter(lambda x:isinstance(x,str),kargs)
    #收集长度
    len_lis = [len(x) for x in lis]

    if len_lis:
    		min_index = min(len_lis)
    		return lis[len_lis.index(min_index)]
    return None

assert short_str(222,1111,'xixi','hahahah') == "xixi"
assert short_str(7,'name','dasere') == 'name'
assert short_str(1,2,3,4) == None

#mys
def short_str2(*args):
    list = filter(lambda x:isinstance(x,str),args)
    print list
    list_len = [len(x) for x in list]
    print list_len
    min_len = min(list_len)
    print min_len
    print list[list_len.index(min_len)]
       
    
short_str2(222,1111,'xixi','hahahah')

#定义一个func(name=None,**kargs),该函数效果如下。
#assert func(“lilei”) == "lilei"
#assert func("lilei",years=4) == "lilei,years:4"
#assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"

def func_absl(name=None, **kargs):
    if kargs=={}:
        print name
    else:
        print name
        print kargs
    a = []
    for (k,v) in kargs.items():
        a.append(k+":"+str(v))
    a.insert(0,name)
    print a 
        
name = "zhangshuo"

func_absl(name,keys='rich',years=55,body='good')


