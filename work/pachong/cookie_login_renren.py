import urllib2, urllib, cookielib
from BeautifulSoup import BeautifulSoup
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