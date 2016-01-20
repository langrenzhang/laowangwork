#coding=utf-8

from sys import argv
#python stupid_file.py zhangshuo /home/zhangshuo/a.txt
filename ,myname, filepath = argv
print filename
print myname
#filepath = '/home/zhangshuo/a.txt'
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
with open(filepath) as txt:
    print txt.read()

#print "Type the filename again:"
#file_again = raw_input(">>>>")

#with open(file_again) as txt2:
#    print txt2.read()
