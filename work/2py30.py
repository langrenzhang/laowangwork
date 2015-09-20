#coding=utf-8
#import threading
#import time
#import re
import urllib

'''
studyer:  zhangshuo
learning: wsgi

查看python位置方法：
1、 查询软件安装路径
在Linux操作系统中查看软件安装路径是通过whereis 命令，如查看php软件的安装路径时输入命令：
   whereis python

2、查询运行文件所在地址（文件夹地址）
查询软件文件夹地址的方法是通过which命令。如查看php文件夹的地址：
    which python

    
Python的强大，其中一个重要原因是Python有很丰富的库（模块）从而可以比较方便地处理各种各样的问题。
Python的第三方modules一般都安装在一些固定的路径，如下：
Unix(Linux): prefix/lib/pythonX.Y/site-packages 默认路径：/usr/local/lib/pythonX.Y/site-packages
Windows:	prefix\Lib\site-packages 默认路径：C:\PythonXY\Lib\site-packages
另外，在Unix-like系统上，Python自身build-in的模块一般位于：/usr/lib/pythonX.Y/site-packages
从源代码安装模块的命令一般为：setup.py install
当然，可以根据需要改变默认的第三方模块安装路径，在命令中可以加上参数：–user, or –home, or –prefix and –exec-prefix, or –install-base and –install-platbase 等来指定安装路径。
需要注意的是：模块的安装路径一定要在 sys.path 这个List中，才能在脚本中可以正常地 import 进来。

关于模块的装， Python官方参考文档是：

http://docs.python.org/3.3/install/index.html#how-installation-works

另外，在Debian系列（包括Ubuntu）的Linux上，一般采用 dist-packages 而不是采用 site-packages 目录；Debian项目的网站上，也对此作了说明，详见：

http://wiki.debian.org/Python#Deviations_from_upstream


下面是我的系统上看到的Python模块的一些路径：

# 在一台RHEL6.3 x86-64系统上
[root@jay-linux ~]# cat /etc/issue
Red Hat Enterprise Linux Server release 6.3 (Santiago)
Kernel \r on an \m
 
[root@jay-linux ~]# ls /usr/lib/python2.6/site-packages/
[root@jay-linux ~]# ls /usr/lib64/python2.6/site-packages/
[root@jay-linux ~]# ls /usr/local/lib64/python2.6/site-packages/
 
# 切换到一台Ubuntu x86-64系统上
master@jay-intel:~$ cat /etc/issue
Ubuntu 12.04.1 LTS \n \l
 
master@jay-intel:~$ ls /usr/lib/python2.7/dist-packages/
 
master@jay-intel:~$ ls /usr/local/lib/python2.7/dist-packages/
easy-install.pth  mysql_connector_repackaged-0.3.1-py2.7.egg
 
master@jay-intel:~$ python3
Python 3.2.3 (default, Oct 19 2012, 20:10:41)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/usr/local/lib/python3.2/dist-packages/mysql_connector_repackaged-0.3.1-py3.2.egg', '/usr/lib/python3.2', '/usr/lib/python3.2/plat-linux2', '/usr/lib/python3.2/lib-dynload', '/usr/local/lib/python3.2/dist-packages', '/usr/lib/python3/dist-packages']
>>>

'''

