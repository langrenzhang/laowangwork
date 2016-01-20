#coding=utf-8

filepath = 'test.txt'

lines = "ZHANG SHUO \nLOVE \nSHI WEN JING \n"

with open(filepath, 'w') as a:
    
    a.write(lines)
    print 'ok'
