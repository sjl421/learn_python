###1、('字典的格式化字符串')
print('1、字典的格式化字符串')
phonebook={'joe':'1023','bob':'2301'}
print("joe's number is %(joe)s"%phonebook)


###2、clear()清除字典中所有的项，原地操作、无返回值
print()
print('2、clear()清除字典中所有的项，原地操作、无返回值')
print('例一')
x={}
y=x
x['key']={'value'}
print (y)
x={}#将X关联到一个新的空列表，不影响y
print(x)
print(y)

print('例二')
x={}
y=x
x['key']={'value'}
print (y)
x.clear()
print(x)
print(y)


###3、fromkeys方法是用给定的键建立新的字段，每个键都对应默认值None
print()
print('3、fromkeys方法是用给定的键建立新的字段，每个键都对应默认值None')
print({}.fromkeys(['name','age']))

print()
print('可在dict上调用fromkeys')
print(dict.fromkeys(['name','age']))

print()
print('不使用none，也可以给默认值')
print(dict.fromkeys(['name','age'],'默认值'))


###4、get()，获取字典项，当用get访问不存在的项时，不会报错，会返回None,还可以自定义返回值替换None
print()
print('4、get()，获取字典项，当用get访问不存在的项时，不会报错，会返回None,还可以自定义返回值替换None')
d={'key':'wakaka'}
print (d.get('key'))
print (d.get('key2'))
print (d.get('key2','没找到'))


###5、items方法将字典所有的项以列表方式返回，3.0为返回迭代器
print()
phonebook1={'joe':'1023','bob':'2301'}
print('5、items方法将字典所有的项以列表方式返回，3.0为返回迭代器')
print(phonebook1.items())

###6、keys方法将字典所有的项以列表方式返回，3.0为返回迭代器
print()
phonebook1={'joe':'1023','bob':'2301'}
print('6、keys方法将字典所有的项以列表方式返回，3.0为返回迭代器')
print(phonebook1.keys())

###7、pop方法用来获得给定键的值，然后将这个键值对从字典中移除
print()
phonebook1={'joe':'1023','bob':'2301'}
print('7、pop方法用来获得给定键的值，然后将这个键值对从字典中移除')
print(phonebook1.pop('joe'))
print(phonebook1)


###8、popitem方法弹出字典随机的项
print()
phonebook1={'joe':'1023','bob':'2301'}
print('8、popitem方法弹出字典随机的项')
print (phonebook1)
print(phonebook1.popitem())
print(phonebook1)


###9、setdefault获取给定键相关联的值，还能在字典不含给定键的时候设定相应的键值
print()
print('9、setdefault获取给定键相关联的值，还能在字典不含给定键的时候设定相应的键值')
d={}
d.setdefault('name','N/A')
print (d)
d['name']='joe'
d.setdefault('name')
print (d)


###10、update利用一个字典项更新另一个字典
print()
print('10、update利用一个字典项更新另一个字典')
phonebook1={'joe':'1023','bob':'2301'}
phonebook2={'joe':'AAAA'}
phonebook1.update(phonebook2)
print (phonebook1)
phonebook3={'amy':'CCC'}
phonebook1.update(phonebook3)
print (phonebook1)

###11、value返回字典的值(3.0版本去掉此函数)
print()
print('11、value返回字典的值(3.0版本去掉此函数)')
phonebook1={'joe':'1023','bob':'2301','a':'sd','f':'dgfhf'}
##print (phonebook1.value())

print('采用in处理')
str1=''
for x in phonebook1:
    print(phonebook1[x])
    str1=str1+(phonebook1[x])+','
print (str1)
print (str1[:-1].split(','))



#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()



#所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。

#那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代
isinstance([1,2,3], Iterable) # list是否可迭代
isinstance(123, Iterable) # 整数是否可迭代


#最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)








