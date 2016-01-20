#coding=utf-8

from sys import argv

script, user_name, password = argv
promt = '>>>'
print "The script is called:",script
print "Your first variable is :",user_name
print "Your second variable is :",password

print "what is %s like ?"%user_name
like = raw_input(promt)
print "you like is :",like

#python stupid_2.py first 2nd 3rd


