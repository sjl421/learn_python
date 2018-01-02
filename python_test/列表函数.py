# -*- coding: cp936 -*-
print ('-----删除序列元素')
list=['a','b','c','d']
del list[2]
print (list)

print ('-----修改序列')
list=['a','b','c','d']
list[2:]=[1,2,3]
print (list)

print ('-----插入序列')
list=['a','b','c','d','e','f']
list[2:4]=[1,2]
print (list)

list=['a','b','c','d','e','f']
list.insert(3,[2,3])
print (list)

print ('-----删除序列')
list=['a','b','c','d','e','f']
list[2:]=[]
print (list)

print ('-----count统计值出现次数')
list=[1,2,3,3,4,5]
print (list.count(3))

print ('-----len函数')
list=[1,2,3,3,4,5]
print (len(list))


print ('-----append函数,列表后追加')
list=[1,2,3,3,4,5]
list.append([9,8])
print (list)


print ('-----extend函数，两个函数相加')
list1=[1,2,3]
list2=[4,5]
list1.extend(list2)
print (list1,id(list1))
print (list2,id(list2))


print ('-----pop函数，删除指定位置元素')
list=[1,2,3,3,4,5]
list.pop()
print (list)
list.pop(2)
print (list)


print ('-----remove函数，删除第一个指定元素')
list=[1,2,3,3,4,5]
list.remove(2)
print (list)
#删除所有元素3
while 3 in list:
    list.remove(3)
print (list)

print ('-----index函数，从列表中找出与某个元素匹配的第一个匹配项的位置')
list=[1,2,3,3,4,5]
print (list.index(3))



print ('-----reverse函数，翻转列表')
list=[1,2,3,3,4,5]
list.reverse()
print (list)

print ('-----sort队员列表进行排序')
list=[6,0,3,3,4,5]
list.sort()
print (list)
print ('关键字reverse()排序')
list=[6,0,3,3,4,5]
list.sort(reverse=True)
print (list)
list.sort(reverse=False)
print (list)
print ('关键字排序：key,长度len()排序')
list=['a','aaa','aa']
list.sort(key=len)
print (list)


print ('-----cmp函数,比较两个元素的大小.（1）两个元素相同返回0，前大后小返回1，前小后大返回-1\
   （2）比较的对象是元素首个字符的ascii值--3.0版本去掉了此函数，如需使用采用（a<b\a>b）')

'''
print (cmp(3,4))
list=[6,0,3,3,4,5]
list.sort(cmp)
print (list)

print (cmp('aaaa',1))
print (cmp(4,3))
list=[6,0,3,3,4,5]
list.sort()
print (list)
'''
a=1
b=2
print(a>b)


print ('-----set函数,列出列表中不重复的元素（去重）集合。\
利用set() 函数后就变成了集合，集合例元素无序')
list=[6,0,3,3,4,5]
list2=set(list)
print (list2)
 



