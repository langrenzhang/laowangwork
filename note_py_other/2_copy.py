import copy
x = object()
l = [x]
l2 = copy.copy(l)
l3 = copy.deepcopy(l)
print "l :",l
print "l2:",l2
print "l2 is l:",l2 is l
print "l2[0] is x:",l2[0] is x
print "l3 is l:",l3 is l
print "l3[0] is x:",l3[0] is x



