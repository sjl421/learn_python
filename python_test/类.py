class Person:
    
    def setName(self,name):
        self.name=name
        
    def getName(self):
        return self.name
    
    def greet(self):
        print ("hello world!I'm %s." %self.name)

foo=Person()
bar=Person()
foo.setName('Mike')
bar.setName('Tom')
foo.greet()
bar.greet()
print (foo.name)
foo.name='Jack'
foo.greet()



class bird:
    song='guagua'
    def sing(self):
        print (self.song)

bird1=bird()
bird1.sing()
birdsong=bird1.sing
birdsong()
print (bird.song)


print('私有化')
class secretive:
    def __inaccessible(self):
        print ("Bet you can't see me")

    def accessible(self):
        print ("The secret message is")
        self.__inaccessible()

s=secretive()
##s.__inaccessible()
s.accessible()
s._secretive__inaccessible()




