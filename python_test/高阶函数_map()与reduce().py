'''
map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。


reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

'''
#请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def prod(L):
    def qj(x,y):
        return x*y
    return reduce(qj,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    L1 = name[0].upper() + name[1:len(name)].lower()
    return L1 
L1 = ["adam","LISA","barT"]
L2 = list(map(normalize,L1))
print (L2)



#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：


# -*- coding: utf-8 -*-
from functools import reduce


def str2float(s):
    def fn1(x, y):
        return x * 10 + y
    def fn2(x, y):
        return x * 0.1 + y
    m = s.find('.')
    L1 = s[:m]
    L2 = s[-1:m:-1]
    def char2num(m):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[m]
    return reduce(fn1, map(char2num, L1)) + reduce(fn2, map(char2num, L2)) * 0.1

print('str2float(\'123.456\') =', str2float('123.456'))




