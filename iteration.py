#coding= utf-8

a = [1, 2, 3, 4, 5]
b = ('a', 'b', 'd')
c = {'name': 'zhangshuo', 'age': '45', 'work': 'coder'}
d = {'a': 'zhangshuo', 'b': '45', 'c': 'coder'}

d_list = d.keys()
d_list.sort()
for x in d_list:
    print x, ':', d[x]
    
    

for x in a:
    print x 
    
for x in b:
    print x 
 
for x, y in c.items():
    print x,':',y
    