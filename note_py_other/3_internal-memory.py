import sys
class User(object):
    def __del__(self):
        print "will be dead!"
        
a = User()
b = a
print "count(a):",sys.getrefcount(a)
del a
print "count(b):",sys.getrefcount(b)
del b


