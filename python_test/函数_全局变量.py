print('1、嵌套作用域')
def a1(x):
     def a2(y):
         print (x+y)
         print ('x:',x)
         print ('y:',y)
     return a2
ddd=a1(2)
ddd(5)
a1(2)(3)


print('')
print('2、全局变量')

x=10
def change_global():
    global x
    x=x+1
    return x
print(change_global())


y='wakaka'
def combin(y):
    print (y+globals()['y'])
combin('haha')
