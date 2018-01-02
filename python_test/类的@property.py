class Screen(object):

'''@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：'''

    @property 
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        self._width=value	
		
    @property
    def height(self):
        return self._height    
		
    @height.setter
    def height(self,value):
        self._height=value
     
    @property
    def resolution(self):
        return self._width*self._height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
