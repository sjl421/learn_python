'''
和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。

注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
所以要强迫filter()完成计算结果，
需要用list()函数获得所有结果并返回list。
'''


#用filter求素数
def _odd_iter():#先构造一个从3开始的奇数序列
    n = 1
    while True:
        n = n + 2
        yield n
        

def _not_divisible(n):#定义一个筛选函数
    return lambda x: x % n > 0


def primes():#定义一个生成器，不断返回下一个素数
    yield 2
    print('y2')
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列 

'''
这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。

由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
'''
for n in primes():
    if n < 1000:
        print(n)
    else:
        break




'''练习：回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
请利用filter()滤掉非回数：'''
# -*- coding: utf-8 -*-

def is_palindrome(n):
    return str(n)==str(n)[::-1]

    
# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))


