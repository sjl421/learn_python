# -*- coding: utf-8 -*-

print ('find函数，从较长的字符串中找到子字符串，返回最左端索引，没找到返回-1')
str11='abcfindabcd'
print (str11.find('find'))
print (str11.find('find',4)) #提供起点
print (str11.find('find',2,-1)) #提供起点和终点


print ('#########################################################')
print ('join函数，用来在队列中添加元素，是split的逆方法')
str1=['1','2','3','4','5']
seq='+'
print (seq.join(str1))

str1='abcde'
seq='+'
print (seq.join(str1))

str1=('d','c','a')
seq='+'
print (seq.join(str1))

str1={'1':'asd','y':2,'z':3}
seq='+'
print (seq.join(str1))


print ('#########################################################')
print ('lower方法返回字符串小写字母（大写为upper()）')
str1='ABCDedf'
print (str1.lower())


print ('#########################################################')
print ('replace方法返回某字符串的所有匹配项均被替换后得到的字符串')
str1='this is replace'
print (str1.replace('is','ass'))


print ('#########################################################')
print ('split将字符串分割为序列')
str1='this is split'
print (str1.split(' '))



print( '#########################################################')
print ('strip将字符串两端的空格去掉')
s1='  this is strip  '
print (s1.strip())


print ('#########################################################2.7版本maketrans函数')
'''print ('translate替换字符串中多个字符')
from string import maketrans
table=maketrans('cs','kz')#将abcd替换为dqfc
print (len(table))
print ('转换后的字母表')
print (table[97:123])
print ('没转换过的字母表')
print (maketrans('','')[97:123])
print ('this is test function'.translate(table))
print ('this is test function'.translate(table,' ')) #第二个参数为指定要删除的字符'''

print ('#########################################################3.0版本内嵌maketrans函数，无需导入')
a='this is test function'
print (a.maketrans('cs','kz'))
p=(a.maketrans('cs','kz'))
print (a.translate(p))


b='this is test function'
print (a.translate({115: 124, 99: 105}))


print('')
map = str.maketrans('123','abc', '78')#要删除的字符需要在这指定
print (map)
s = '54321123789'
print (s.translate(map))















