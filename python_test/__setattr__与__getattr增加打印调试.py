
class Rec:
    def __init__(self):
        print ('init1')
        self.width=0
        self.height=0
        print ('init')
        print ('')
    def __setattr__(self,name1,value):
        if name1=='size':
            self.width=value
            self.height=value
            print('set if')
        else:
            
            self.__dict__[name1]=value
            print ('set else')
            print(name1,value)
            print ( self.__dict__[name1])
    def __getattr__(self,name1):
        if name1=='size':
            print ('get if')
            return self.width,self.height
        else:
            raise AttributeError

c=Rec()
print ('wawawa')
c.size=123
print ('kakaka')
#c.arr=666
print (c.size)
#print (c.arr)
print (c.width,c.height)


print ('---------------------')


class Book(object):
    def __setattr__(self, name1, value1):
        if name1 == 'value':
            object.__setattr__(self, name1, value1 - 100)
            print ('set if')
        else:
            object.__setattr__(self, name1, value1)
            print ('set else')
    def __getattr__(self, name1):
        try:
            print ('__getattr__ try')
            return object.__getattribute__(name1)
            
        except:
            return name1 + ' is not found!'
    def __str__(self):
        print ('__str__')
        return self.name1 + ' cost : ' + str(self.value1)

c = Book()
print ('c = Book()')
c.name = 'Python'
print ('Python')
c.value = 100
print ('--')

print (c.name)
print ('++')
print (c.value1)

#print (c)

#print (c.Type)
