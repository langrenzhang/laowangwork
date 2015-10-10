#coding=utf-8
from django.http import HttpResponse
def home(request,id):
#    return HttpResponse('Hi,zhangshuo,world')  #这里不允许使用print输出要用这个方法，而且只能输出字符串
    return HttpResponse('id is %s'%id) 
