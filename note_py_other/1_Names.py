#coding=utf-8
import sys
x = 211
y = "Hi zhangshuo"
z = x

print "x is z:",x is z
print "globals():",globals()
print "locals()",locals()

def test(x):
    y = x+100
    print locals()
    print globals() is locals()
    frame = sys._getframe(0)
    print locals() is frame.f_locals

test(123)

a = object()
b = a 
print a is b 
print id(a)
print hex(id(a))
print id(b)
print hex(id(b))
