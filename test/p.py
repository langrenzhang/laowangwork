#coding= utf-8


#
#def ten(x, y=2):
#    ' number is good '
#    print x 
#    print y
#    return [y*11 for y in range(1, x+1)]
#x = input()
#print ten(x, y=2)
#
#print ten.__doc__   #wen dang

#b = 3
#def a():
#    return b 
#    
#    
#def c():
#    global b
#    b = 8
#    return b  
#def d():
#     
#    return b 
#def e():
#    b = 3
#    return b
#
#print a()
#print c()
#print d()
#print e()
#print b
#

#
#def a(**kr):
#    return kr
#
#print a(a=2,b=3,c='e',d='w')
#
#def b(*kr):
#    return kr
#
#print b(1,2,'d')
#
#def test(c,w,*k,**kr):
#    return k,kr
#
#print test(1,2,3,4,'ds',a=1,b=2)


#########################################

a = 123
b = 3434
c = 3
def cmptest(a, b, c):
    if a>b:
        if a>c:
            print a 
        else:            
            print c
    elif a<b:
        if b>c:
            print b 
        else:
            print c            
    elif b>c:
        print b 
    else:
        print c         
cmptest(a, b, c)
x=88
y=22
z=44
def ainfo(*k):
    w = sorted(list(k))
    return w 
print ainfo(x, y, z)

def cinfo(*kr):
    g = list(kr)
    for i in range(len(g)):
        print g[i]  
        
cinfo (x, y, z)
