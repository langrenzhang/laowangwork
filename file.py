#coding= utf-8

f = open('a.txt', 'w')
f.write('zhagnshuo\nwoainimen')
f.close()


with open('a.txt', 'a') as f:
    f.write('\nhahahahh')
