# -*- coding: utf-8 -*-


#请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
   
    return t[0].lower()


L2 = sorted(L, key=by_name)
print(L2)



#再按成绩从高到低排序：
def by_score(t):
    return t[1]

L = [("Bob",75),("Adam",92),("Bart",66),("List",88)]
L2 = sorted(L,key=by_score)
print(L2)



#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
