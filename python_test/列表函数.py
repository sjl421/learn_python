# -*- coding: cp936 -*-
print ('-----ɾ������Ԫ��')
list=['a','b','c','d']
del list[2]
print (list)

print ('-----�޸�����')
list=['a','b','c','d']
list[2:]=[1,2,3]
print (list)

print ('-----��������')
list=['a','b','c','d','e','f']
list[2:4]=[1,2]
print (list)

list=['a','b','c','d','e','f']
list.insert(3,[2,3])
print (list)

print ('-----ɾ������')
list=['a','b','c','d','e','f']
list[2:]=[]
print (list)

print ('-----countͳ��ֵ���ִ���')
list=[1,2,3,3,4,5]
print (list.count(3))

print ('-----len����')
list=[1,2,3,3,4,5]
print (len(list))


print ('-----append����,�б��׷��')
list=[1,2,3,3,4,5]
list.append([9,8])
print (list)


print ('-----extend�����������������')
list1=[1,2,3]
list2=[4,5]
list1.extend(list2)
print (list1,id(list1))
print (list2,id(list2))


print ('-----pop������ɾ��ָ��λ��Ԫ��')
list=[1,2,3,3,4,5]
list.pop()
print (list)
list.pop(2)
print (list)


print ('-----remove������ɾ����һ��ָ��Ԫ��')
list=[1,2,3,3,4,5]
list.remove(2)
print (list)
#ɾ������Ԫ��3
while 3 in list:
    list.remove(3)
print (list)

print ('-----index���������б����ҳ���ĳ��Ԫ��ƥ��ĵ�һ��ƥ�����λ��')
list=[1,2,3,3,4,5]
print (list.index(3))



print ('-----reverse��������ת�б�')
list=[1,2,3,3,4,5]
list.reverse()
print (list)

print ('-----sort��Ա�б��������')
list=[6,0,3,3,4,5]
list.sort()
print (list)
print ('�ؼ���reverse()����')
list=[6,0,3,3,4,5]
list.sort(reverse=True)
print (list)
list.sort(reverse=False)
print (list)
print ('�ؼ�������key,����len()����')
list=['a','aaa','aa']
list.sort(key=len)
print (list)


print ('-----cmp����,�Ƚ�����Ԫ�صĴ�С.��1������Ԫ����ͬ����0��ǰ���С����1��ǰС��󷵻�-1\
   ��2���ȽϵĶ�����Ԫ���׸��ַ���asciiֵ--3.0�汾ȥ���˴˺���������ʹ�ò��ã�a<b\a>b��')

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


print ('-----set����,�г��б��в��ظ���Ԫ�أ�ȥ�أ����ϡ�\
����set() ������ͱ���˼��ϣ�������Ԫ������')
list=[6,0,3,3,4,5]
list2=set(list)
print (list2)
 



