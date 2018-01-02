
class Rec:
    
    def __init__(self):
        print ('init begin ')
        
        self.width=0
        self.height=0
        
        print ('init end')
        print ('')
        
    def __setattr__(self,name1,value):
        if name1=='size':
            print('set if begin')
            
            self.width=value
            self.height=value
            
            print('set if end')
            print ('')
            
        else:
            self.__dict__[name1]=value
            print ('set else begin')
            print(name1,value)
            print ( self.__dict__[name1])
            print ('set else end')
            
    def __getattr__(self,name1):
        
        if name1=='size':
            print ('get if')
            return self.width,self.height
        else:
            raise AttributeError

c=Rec()
print ('wawawa')
c.size=123
print ('wawawa')
print (c.size)

