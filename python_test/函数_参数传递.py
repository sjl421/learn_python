print('1、收集参数')


def test(x,y,z,*p,**d):
    print (x)
    print (y)
    print (z)
    print (p)
    print (d)
test(1,2,3,1,2,3,4,5,6)
test(1,2,3,1,2,3,4,a=5,b=6)


print('')
print('2、收集参数逆过程')

def add(x,y):
    print(x+y)
p=(2,3)
add(*p)


def printer(name,age):
    print ('his name is %s age is %d' %(name,age))
p=('TOM',3)  
printer(*p)


def printer(name='jay',age=12):
    print ('his name is %s age is %d' %(name,age))
p={'name':'BOB','age':23}  
printer(**p)


