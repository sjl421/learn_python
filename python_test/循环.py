d={'a':'1','b':'2'}
for key ,value in d.items():
    print (key,'and',value)
print (d.items())

d={'a':'1','b':'2'}
for key ,value in d.items():
    if key=='b':
        d[key]=112        
print (d)



#并行迭代，zip可将两个序列压缩在一起，返回一个元组的列表
print ('')
print ('循环解包')
names=['joy','tom','bob']
ages=[32,22,45]
print (zip(names,ages))
for name,age in zip(names,ages):
    print (name,'is',age)


#按索引迭代
print ('')
print ('按索引迭代')
strings=['xxx','x2','xxx','xxx','d2']
for string in strings:
    if 'xxx' in string:
        index=strings.index(string)
        strings[index]='rep'
print (strings)


strings=['xxx','x2','xxx','xxx','d2']
index=0
for string in strings:
    if 'xxx' in string:
       strings[index]='rep'
    index+=1   
print (strings)


strings=['xxx','x2','xxx','xxx','d2']
for index1,string1 in enumerate(strings):
    if 'xxx' in string1:
        strings[index1]='rep'
print (strings)



#反转和排序迭代
print ('')
print ('反转和排序迭代')
a=[6,2,3,4,5,1]
print (sorted(a))
print (a)
b=['h','e','l','l','o','w','o','r','l','d']
print (list(reversed(b)))
print (' '.join(reversed(b)))


while True:
    word=input('input word:')
    if not word:
        break
    print('the word is:',word)



    
for n in range(10):
    if n==11:
        break
else:
    print('not break')


#列表推导式
print ('')
print ('列表推导式')
print ([x*x for x in range(10)])
print ([x*x for x in range(10) if x%3==0])
print ([(x,y) for x in range(3) for y in range(3)])
#####
girls=['alice','bernice','clarice']
boys=['chris','arnold','bob']
print( [b+'+'+g for b in boys for g in girls if b[0]==g[0]] )
print( [b+'+'+g for b in boys for g in girls] )

print(chr(97))



