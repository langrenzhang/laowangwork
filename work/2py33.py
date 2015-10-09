#coding=utf-8
'''
进阶结束第二课


1.学会如何去分解问题 把大问题分解成小问题

1.1 如何去发微博 使用新浪的开发者账号 
1.2 如何去采集 京东的 搜索列表信息
        1.2.1 可以根据页面和关键字采集到内容
        1.2.2 解析内容 beautifulsoup
        1.2.3 检查

        http://p.3.cn/prices/mgets?skuids=J_1003950123,J_1003375727,J_1003210353,J_1001703444,J_1003026740,J_1000958533,J_1003568005,J_1001699109,J_1002271458,J_1002988376,J_1003108619,J_1000804240,J_1001725613,J_1002785706,J_1002827700,J_1003334496,J_1000288477,J_1002641185,J_1002027262,J_1001726962,J_1002254735,J_1002258867,J_1003665794,J_1002251756,J_1002607622,J_1003505629,J_1002252430,J_1000792197,J_1001834437,J_1003565398,J_1000263920,J_1004044517,J_1002605538,J_1003165200,J_1003294716,J_1003535246,&type=1&callback=jsonp1371298348235&_=1371298349687

'''



import urllib
def get_content_from_jd(keyword,page=1):
    jd_url = 'http://search.jd.com/s.php?keyword=%s&enc=utf-8&area=1&psort=&page=%s&vt=2&qr=&qrst=UNEXPAND&et=&sttr=1'%(keyword,page)
    r = urllib.urlopen(jd_url)
    content = r.read()
    r.close()

    return content,jd_url

print get_content_from_jd('裤子',3)[1]


def get_price_from_ids(*ids):
    pass



def get_res_from_jd(keyword,page=1):
    '''
    [{id:xx,price:xx,detail:xx,title:xx},{id:xx,price:xx,detail:xx,title:xx},{id:xx,price:xx,detail:xx,title:xx}]
    '''


    pass


#print get_content_from_jd('裤子')
