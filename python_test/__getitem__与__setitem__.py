def checkindex(key):
    if not isinstance(key,(int)):
        raise TypeError
    if key<0:
        raise IndexError

class ArithmeticSequence:
    
    def __init__(self, start=0, step=1):
        self.start=start
        self.step=step
        self.change={}


        
    def __getitem__(self, key):
        checkindex(key)
        try:
            print( "try")
            return self.change[key]
        except KeyError:
            print( "KeyError")
            return self.start + key * self.step
        
    def __setitem__(self, key, value):
        checkindex(key)
        self.change[key]=value



s=ArithmeticSequence()
print(s)

print( s[0],s[1],s[2],s[3],s[4] ,s[5])
s[4]=2
print( s[0],s[1],s[2],s[3],s[4] ,s[5])



class WPUnit(object):
    def __init__(self):
        self._res={}

    def __setitem__(self,key,val):
        self._res[key]=val

    def __getitem__(self,key):
        if key in self._res:
            return self._res[key]
        else:
            r=WPUnit()
            self.__setitem__(key,r)
            return r

a=WPUnit()
a['a']['b']['c']['d']['e']['f']['g']=5
print (a['a']['b']['c']['d']['e']['f']['g'])





