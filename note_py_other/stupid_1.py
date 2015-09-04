#coding=utf-8

print "plus,5+4:",5+4
print "5%2:",5%2
print "5/2",5/2
print "float(5)/float(2):",float(5)/float(2)

a = "zhangshuo"
b = "is"
c = "haoren"

print a,b,c
print a+b+c

formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (a,b,c,"hello world")

print "zhangshuo %s" % ("haoren hello")

s = raw_input("what's you name:")
print type(s)
print s

h = raw_input("you height:")
age = raw_input("you age:")

print "my name is : %s ,my height is : %s , my age is : %s"%(s,h,age)

#dos  pydoc os =>> os.help.doc


