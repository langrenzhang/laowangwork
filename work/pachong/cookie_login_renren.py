#coding=utf-8
#! /usr/bin/python
#py2.7

import urllib2, urllib, cookielib
from BeautifulSoup import BeautifulSoup

"""
1.人人网的登录地址需要用BeautifulSoup来抓取。 
2.个人信息存在info中。info是一个字典{'email':'xx','password':'xx'}.key的命名
  需要根据实际网页中定义，比如豆瓣的定义是{'form_email':'xx','form_password':'xx'} 
3.使用cookie的好处在于，登录之后你可以使用cookie中保存的信息作为头信息的一部分，
  利用已经保存的头信息接着访问网站。

#########################
I want to download and parse webpage using python, 
but to access it I need a couple of cookies set. 
Therefore I need to login over https to the webpage first. 
The login moment involves sending two POST params (username, password)
to /login.php. 
During the login request I want to retrieve the cookies from the 
response header and store them so I can use them in the request 
to download the webpage /data.php.


#test1
import urllib, urllib2, cookielib

username = 'myuser'
password = 'mypassword'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'username' : username, 'j_password' : password})
opener.open('http://www.example.com/login.php', login_data)
resp = opener.open('http://www.example.com/hiddenpage.php')
print resp.read()
resp.read() is the straight html of the page you want to open, and you can use opener to view any page using your session cookie.


test2
from requests import session

payload = {
    'action': 'login',
    'username': USERNAME,
    'password': PASSWORD
}

with session() as c:
    c.post('http://example.com/login.php', data=payload)
    response = c.get('http://example.com/protected_page.php')
    print(response.headers)
    print(response.text)

"""

url = 'http://www.renren.com'
#get login url
resp1 = urllib2.urlopen(url)
source = resp1.read()
soup1 = BeautifulSoup(source)
log_url=soup1('form', {'method': 'post'})[0]['action']
#login by cookie
#-info
info = {}
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
#-try log
try:
    resp2 = urllib2.urlopen(log_url, urllib.urlencode(info))
except urllib2.URLError, e:
    if hasattr(e, 'reason'):
        print 'reason:{0}'.format(e.reason)
    if hasattr(e, 'code'):
        print 'code:{0}'.format(e.code)