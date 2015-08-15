#coding=utf-8
import os
import glob
import urllib

'''
print 2
print 4
print 2,
print 4,
print 6,
f = open('f.txt','w')
print f.read()
f.close()
'''

#######################################################################
 
def get_page(u):
        
    a = urllib.urlopen(u).read()
    print a  
   
#    google = urllib.urlopen(u)  
#    print type(google.read())
#    print '#################http header:', google.info()  
#    print '###################http status:', google.getcode()  
#    print '#################url:', google.geturl()  
#    for line in google: # 就像在操作本地文件  
#        print "###########"
#        print line,  
#    google.close()  
    
    
a = "https://www.baidu.com/"


#get_page(a)


#######################################################################


#x = 0
#while x<55: #True do next
#    x += 1
#    print x 
#    '''
#    if x>=50:
#        break
#    '''
#else:
#    print 'end'
#for x in range(1, 11):
#    print x 
#for y in 'I love zhang shuo ,he is my sun.'.split(' '):
#    print y,
#else:
#    print y
#split()  without space and ',' connected string

###################################################

#
#x = 1
#while x<11:
#    print x, 
#    x += 1    
#for y in range(1, 11):
#    if y % 2 == 1:
#        print y,
#    else:
#        continue    
#print '\n'
#a = range(1, 7)
#print a
#if 8 in a:
#    print 'find it in the list'
#else:
#    print 'not find it'
#b = len(a)
#c = []
#i = 0
#while b>=1:
#    c.append(a[i]+1)
#    b=b-1
#    i=i+1    
#print c
#

####################################################
#a = "aAsmr3idd4bgs7Dlsf9eAF"
#print a 
#print a.lower()
#print a.upper()
#print a.swapcase()

#b = []
#c = range(1, 11)
#for x in a:
#    if int(x) in c:
#        print x
#
#b = ''.join([x for x in a if x.isdigit()])
#print b
############################
#a=a.lower()
#b = dict([(x, a.count(x)) for x in set(a)]) # importent
#print b
       
#a_list = list(a)
#set_list = list(set(a_list))
#set_list.sort(key = a_list.index)
#print set_list
#print ''.join(set_list)
################去除a字符串内的数字后，排序a-z保留大小写,a与A的顺序关系为：A在a前面。####

#z_list = []
#for x in a:
#    if not x.isdigit():
#        z_list.append(x)
#        
#z_list = list(set(z_list))
#z_list.sort()
#print z_list
#z_upper_list = []
#z_lower_list = []
#for x in z_list:
#    if x.isupper():
#        z_upper_list.append(x)
#    elif x.islower():
#        z_lower_list.append(x)
#    else:
#        pass
#print z_upper_list 
#print z_lower_list
#for y in z_upper_list:
#    y_low = y.lower()
#    if y_low in z_lower_list:
#        z_lower_list.insert(z_lower_list.index(y_low), y)
#                       
#print z_lower_list

#######################################################################
#
#file_open = open('twitter-test.txt', 'r')
##print f.readline()
#file_out = file_open.readline()
#print file_out 
#
#file_make = file_out.split(',')
#
#print len(file_make)
#print file_make[2].
##print 'w'
##print f.readline()
#
#
#file_open.close()

#######################################################################


#######################################################################


#######################################################################


#######################################################################


#######################################################################


#######################################################################

