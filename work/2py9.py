#coding=utf-8
import os
import urllib
import random
import string
'''
高级语言通常都内置了一套try...except...finally...的错误处理机制
'''
#try:
#    print 'try...'
#    r = 10 / 0
#    print 'result:', r
#except ZeroDivisionError, e:
#    print 'except:', e
#finally:
#    print 'finally...'
#print 'END!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

# get url save as file
def save_url_path(url, folder = None):
    if not (url.startswith('http://') or url.startswith('https://')):
        return "url is error"
    if not os.path.isdir(folder):
        return "path is error"    
    a = urllib.urlopen(url)
    content = a.read()
    print content
    random_filename = "test_%s.txt"%random.randint(1, 1000)
    file_path = os.path.join(folder, random_filename)
    d = open(file_path, 'w')
    d.write(content)
    d.close()
    return file_path    
#print save_url_path('http://www.baidu.com', '/tmp')

# get all file name

def get_filename(filepath):
    if not os.path.exists(filepath):
        return "filename is error"
    for f in os.listdir(filepath):
        print f
    
get_filename('/tmp/deepdream-master')