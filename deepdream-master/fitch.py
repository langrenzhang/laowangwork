#coding=utf-8

with open('phone1.txt', 'r') as fil1:
    a = fil1.readlines()

with open('phone2.txt', 'r') as fil2:
    b = fil2.readlines()

print type(b[0])  
ps = []
for i in a:
    for j in b:
        if i == j:
            ps.append(i) 
with open('w.txt', 'w') as file3:
    c = file3.write(w)
