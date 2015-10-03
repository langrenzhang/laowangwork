#coding=utf-8
#import threading
#import time
#import re
#import urllib

"""

童鞋们好，我们的进阶课终于要讲完了。这里，留给大家一道进阶篇的结束题。要求如下：


【准备步骤】
1.申请一个微博的开发者账号，http://open.weibo.com/apps
2.为新申请的开发者账号，添加几个测试账号
3.找到新浪的python sdk 



【需求】

1.已知一个网站 http://c/，网站名为 “鞋推网”
2.网站使用微博的账号密码登陆。
3.登陆成功后，显示京东网 搜索 鞋子 的第一页结果列表。（如果能分页肯定更好了，但不强求）

3.1 结果列表中需包含图片，名字。
3.2 图片需存储在本地。


4.点击列表中的任意一个图片后，立即分享到新浪微博。（使用哪个账号登陆，就使用那个账号发一个微博）微博内容如下

“我在鞋推网为我推荐了一双鞋子[鞋子的名字]，哈哈。http://c/”
此信息后附一张鞋图片


【完成】
给大家10天的时间。之后我们开始讲解这道结业题。


这道题综合了我们以前所有的知识。

"""

"""
授权步骤（居于oauth2）：

1 生成第三方url,跳转过去让用户对我们的应用授权

APP_KEY = '3512831944'            # app key
APP_SECRET = 'c477697108b5f856f0f38e979ffa79c1'      # app secret
CALLBACK_URL = 'http://www.github.com/langrenzhang'  # callback url

2 授权成功后，跳转到callback_url里，传一个code参数。
"""

from weibo import APIClient
#from weibo import TwitterMixin      #error: suppose you are using Twitter


APP_KEY = '3512831944'            # app key
APP_SECRET = 'c477697108b5f856f0f38e979ffa79c1'      # app secret
CALLBACK_URL = 'http://www.github.com/langrenzhang'  # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

url = client.get_authorize_url()    # redirect the user to 'url'

print url



"""
r = client.request_access_token(SOME_CODE)
access_token = r.access_token  # access token，e.g., abc123xyz456
expires = r.expires      # token expires time, UNIX timestamp, e.g., 1384826449.252 (10:01 am, 19 Nov 2013, UTC+8:00)
NOTE: you should store the access_token for later use.
"""