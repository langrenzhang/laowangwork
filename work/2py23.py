#coding=utf-8

'''
返回素数：如果p是素数则为True，否则为假
'''
def is_prime(p):
    if p == 1:
        return False
    if p == 2:
        return True
    else:
        for i in xrange(2, p):
            if p%i == 0:
                return False 
        return True            

#语句
#for i in xrange(1, 101):
#    if is_prime(i):
#        q.append(i)   

#列表生成式
#q = [i for i in xrange(1, 101) if is_prime(i)]
#print q

#函数化
#def num_auto(numax):
#    return [i for i in xrange(1, numax+1) if is_prime(i)]#注意
print num_auto(5000)
    
    
'''
用yied求1000000000000后100个素数

'''


         



