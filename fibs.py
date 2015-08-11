#coding=utf-8
#返回斐波那契数列列表的函数的定义 
def fibs(m):
    result = [0, 1]
    for i in range(m-2):
        result.append(result[-1]+result[-2])
    return result
m = input()
print fibs(m)