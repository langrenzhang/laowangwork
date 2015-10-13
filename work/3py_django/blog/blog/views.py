#coding=utf-8
from django.http import HttpResponse
import datetime

def home(request):
#    return HttpResponse('Hi,zhangshuo,world')  #这里不允许使用print输出要用这个方法，而且只能输出字符串
#    return HttpResponse('id is %s'%id) 
#    return HttpResponse('赵小宁同学：\n    该吃饭了')


    now = datetime.datetime.now()
    html = "<html><body>智贤同学，这个时间：%s.==>>该吃药了..^-^</body></html>" % now
    return HttpResponse(html)

