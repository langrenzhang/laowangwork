#coding=utf-8
#! /usr/bin/python

import re
import urllib
#import urllib2

""" doc 主要用正则来处理数据爬取图片"""

def get_content(url):
    """doc"""
    html = urllib.urlopen(url)
    content = html.read()
#    print html.getcode()
    html.close()
    return content

def get_image(info):
    
    """doc
     http://tieba.baidu.com/p/3906256674
    """
    
    reg = r'class="BDE_Image" src="(.+?\.jpg)"'
#    reg = r'img src="(.+?\.jpg)"'
    pat = re.compile(reg)
    image_code = re.findall(pat, info)
    
    i = 1
    for image_url in image_code:
#        image_url = "".join(["http:",image_url])
        print image_url
#        图片下载函数 urlretrieve 函数
        urllib.urlretrieve(image_url, '萌妹子%s.jpg' % i)
        i += 1        

#    return image_code

#urls = "http://tieba.baidu.com/p/3906256674"
urls = "http://tieba.baidu.com/p/3987804351"
#urls = "http://tieba.baidu.com/p/3140779423#!/l/p1"


info = get_content(urls)
#info = get_content("http://www.zhihu.com/question/29134042")
get_image(info)