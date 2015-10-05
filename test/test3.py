'''
去重和list拼接
'''

a = ["a","b","c"]
print a

b = ["d","e","a","c"]
a.extend(b)
print a

a = list(set(a))
print a