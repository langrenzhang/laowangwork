#coding=utf-8

"""
#coding=utf-8

'''
django web编程扫盲之二


1.为什么我只能做到这步？



2.web码农三步问：

    2.1 web码农问题之一：web编程的核心是什么？ 折腾database


    2.2 web码农问题之二：web编程的核心是什么？ 折腾template

    开发逻辑上的折腾： html + css + javascript(ajax) + 浏览器兼容性
    编程思路上的理解：表现 和 内容 分离

    mvc 

    控制器 
    数据 model orm
    展现

    2.3 web码农问题之三：web编程的核心是什么？ 折腾框架

    django :all in one

    flask:

     tornado:知乎

      webpy web2py 

      框架：

      狭义：学习框架 ： 看文档，写项目，看源码，写框架
      
      广义：结构

    总之，就是折腾。


3.来折腾一下下templete,了解一下下非持久存储。

from django.template import Template, Context


template_str =  ""My name is {{ name }}.""




#占位符



t = Template(template_str)

c = Context({"name": "Stephane"})
t.render(c)


接下来的学习重点：http://djangobook.py3k.cn/chapter04/




'''


"""
