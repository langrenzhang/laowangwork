#coding=utf-8
import itertools
"""
learn some def with itertools


"""


#chain 
it = itertools.chain(xrange(3), "abc")
print it 
print list(it)
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

#combinations
it = itertools.combinations("abcd", 2)
print it
print list(it)
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

#combinations_with_replacement
it = itertools.combinations_with_replacement("abcd", 2)
print it
print list(it)
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

it = itertools.compress("abcde", [1,0,1,1,0])
print it
print list(it)
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

for x in itertools.count(10, step = 2):
    print x
    if x > 20:break

print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"


for i,x in enumerate(itertools.cycle("abc")):
    print x
    if i > 7:break

it = itertools.dropwhile(lambda i:i<4,[2,1,4,1,3,8])
print list(it)

it = itertools.takewhile(lambda i:i<4,[2,1,4,1,3,8])
print list(it)


