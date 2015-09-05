#coding=utf-8
#! /usr/bin/python

import re
import urllib
from bs4 import BeautifulSoup

""" doc 主要bs4来爬图片"""

def get_content(url):
    """ doc """
    html = urllib.urlopen(url)
    content = html.read()
    html.close()
    return content


def get_image(info):
    """doc """
    soup = BeautifulSoup(info)
    all_img = soup.find_all('img', class_="BDE_Image")    
    i = 1
    for img in all_img:
        image_name = 'soup%s.jpg' % i
        urllib.urlretrieve(img['src'], image_name)
        i = i+1    

urls = "http://tieba.baidu.com/p/4023095156"
info = get_content(urls)
get_image(info)
