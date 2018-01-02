class bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry==True:
            print ('eat eat eat')
            self.hungry=False
        else:
            print('not hungry')

            
class chicken(bird):
    def __init__(self):
        super().__init__()
        self.song='wo wo wo'
    def sing(self):
        print (self.song)



class chick(chicken):
    def __init__(self):
        super().__init__()
        self.poop='enenen~~'
    def p(self):
        print (self.poop)


        
a=chick()
a.eat()
a.eat()
a.sing()
a.p()
