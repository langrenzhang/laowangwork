#coding=utf-8
import threading
import time
import re
import urllib
import socket


'''
socket
  1,udp,tcp/ip,socket
     HTTP tcp/ip
	 qq
  2，nc：netcat小技巧
  3，服务端/客户端
     3.1，创建 socket对象，socket,socket(1,2)
	    3.1.1, AF_INET和AF_UNIX                       创建对象Internet和Unix，前边基于ip后边基于文件
		3.1.2, SOCK_STREAM tcp/ip SOCK_DGRAM udp      哪种通讯模式，tcp/ip和udp（qq就是这个通讯）
		#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	 3.2 绑定端口 socket.bind(('localhost',8888))
	    #s.bind(('localhost',8125))                    绑定端口，对象是一个tuple，元组
	 3.3 socket.listen(n)
	    n代表允许多少个同时请求
		#s.listen(8)                 				   同时允许八个请求
		
	 3.4 connection,address = sock.accept()
	     connection,address = s.accept()               s.accept() 是一个tuple，是等待请求的对象。  
													   等待请求过程中阻塞在这一行，当有请求的时候，会把请求的对象和地址传递过来tuple
	 3.5 buf = connection.recv(100)
	     buf = connection.recv(10)					   获取10个数据，10<100，不管多少数据，只抓十个。
	 3.6 connection.send(buf)
		 connection.send(buf)						   将获取的十个数据buf抛出
	 3.7 不关闭就惨了 connection.close()			   不要忘了关闭，如果是异地还有超时怎么办。。。
'''

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8125))
s.listen(8)
'''
是一个栈，出栈入栈的过程如下：
10 2
9 10 
[1,2,3,4,5,6,7,8]
跑完一个比如4，后会变成
[1,2,3,5,6,7,8]这个时候9会进去变成
[1,2,3,5,6,7,8,9]
'''

while 1:
    connection,address = s.accept()
    buf = connection.recv(10)
    connection.send(buf)
# 为什么只能运行一次
s.close()






