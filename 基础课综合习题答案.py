#coding=utf-8



#1. ��֪�ַ��� a = "aAsmr3idd4bgs7Dlsf9eAF",Ҫ������
#


a = "aAsmr3idd4bgs7Dlsf9eAF"

#1.1 �뽫a�ַ����Ĵ�д��ΪСд��Сд��Ϊ��д��
#
a = "aAsmr3idd4bgs7Dlsf9eAF"

print a.swapcase()

#1.2 �뽫a�ַ���������ȡ�����������һ���µ��ַ�����
#
a = "aAsmr3idd4bgs7Dlsf9eAF"

print ''.join([s for s in a if s.isdigit()])


'''


[s for s in a if s.isdigit()]


''.join()

'''

#1.3 ��ͳ��a�ַ������ֵ�ÿ����ĸ�ĳ��ִ��������Դ�Сд��a��A��ͬһ����ĸ�����������һ���ֵ䡣 �� {'a':4,'b':2}
#
a = "aAsmr3idd4bgs7Dlsf9eAF"

a = a.lower() 
print dict([(x,a.count(x)) for x in set(a)])

'''

dict([(x,a.count(x)) for x in set(a)])


dict()

[(x,a.count(x)) for x in set(a)]
'''
            
            
#1.4 ��ȥ��a�ַ�����γ��ֵ���ĸ���������ȳ��ֵ�һ������ 'abcabb'������ȥ������� 'abc'
#
a = "aAsmr3idd4bgs7Dlsf9eAF"

a_list = list(a) #ת����list
set_list = list(set(a_list)) #ȥ���Ժ���ת����list
set_list.sort(key=a_list.index) #��ȥ���Ժ��list����ԭ�ȵ�����
print ''.join(set_list)#ƴ�ӳ��ַ���


#1.5 �뽫a�ַ�����ת�����������'abc'�ķ�ת��'cba'
#
a = "aAsmr3idd4bgs7Dlsf9eAF"

print a[::-1] #����

#1.6 ȥ��a�ַ����ڵ����ֺ��뽫���ַ�����ĵ�����������a-z���������������һ���������ַ������������Сд,a��A��˳���ϵΪ��A��aǰ�档����AaBb��
#

'''

1.Ҫ��Сд��ĸ��a-z������
2.��Сд��ͬ����ֵ��ͬ����ĸ,��д��Сд��ǰ��



'''

a = "aAsmr3idd4bgs7Dlsf9eAF"

l = sorted(a)

a_upper_list = []
a_lower_list = []

for x in l:
    if x.isupper():
        a_upper_list.append(x)
    elif x.islower():
        a_lower_list.append(x)
    else:
        pass

for y in a_upper_list:
    y_lower = y.lower()
    if y_lower in a_lower_list:
        a_lower_list.insert(a_lower_list.index(y_lower),y)

print ''.join(a_lower_list)
        


#1.7 ���ж� 'boy'����ֵ�ÿһ����ĸ���Ƿ漳�����a�ַ����������֣������True���������� ��False.
#

a = "aAsmr3idd4bgs7Dlsf9eAF"
search = 'boy'

u = set(a)
u.update(list(search))
print len(set(a)) == len(u)

##���н������swferͬѧ��������graceful����
a = "aAsmr3idd4bgs7Dlsf9eAF"
print set('boy').issubset(set(a))


#1.8 Ҫ����1.7����ʱ�ĵ����жϣ���'boy'��Ϊ�ĸ����ֱ��� 'boy','girl','bird','dirty'�����ж�������4���ַ������ÿ����ĸ���Ƿ漳�����a�ַ����
#


a = "aAsmr3idd4bgs7Dlsf9eAF"
search = ['boy','girl','bird','dirty']

b = set(a)
for i in search:
    b.update(list(i))

print len(b) == len(set(a))


##���н������swferͬѧ��������graceful����
a = "aAsmr3idd4bgs7Dlsf9eAF"
lst=['boy','girl','bird','dirty']
s=''.join(lst)
print set(s).issubset(set(a))




#1.9 ���a�ַ�������Ƶ����ߵ���ĸ

a = "aAsmr3idd4bgs7Dlsf9eAF"


l = ([(x,a.count(x)) for x in set(a)])
l.sort(key = lambda k:k[1],reverse=True)
print l[0][0]


#
#
#2.��python�����������import this �Ժ���ֵ��ĵ���ͳ�Ƹ��ĵ��У�"be" "is" "than" �ĳ��ִ�����
#

import os
m =  os.popen('python -m this').read()
m = m.replace('\n','')
l = m.split(' ')
print [(x,l.count(x)) for x in ['be','is','than']]

#
#3.һ�ļ����ֽ���Ϊ 102324123499123���������ļ�����kb��mb����õ��Ĵ�С��


size = 102324123499123

print '%s kb'%(size >> 10)
print '%s mb'% (size >> 20)

#
#4.��֪  a =  [1,2,3,6,8,9,10,14,17],�뽫��listת��Ϊ�ַ��������� '123689101417'.
#

a =  [1,2,3,6,8,9,10,14,17]


print str(a)[1:-1].replace(', ','')

#