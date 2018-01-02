nested1=[[[1,2],3],[4,[5,6]],[7,8]]
nested=[['a','b'],['c']]
nested2=[[1,2],3]      



def loopfun2(L):
    try:
        print('这是tryL',L)
        for i in L:
            print('这是i',i)
            for j in loopfun2(i):
                print ('这是循环里的',j,'j')
                print ('这是循环里的',i,'i')
                print ('-----')
                yield j
                print ('yield j')
                print ('+++')
    except TypeError:
        print ('yield异常1 L')
        yield('e:',L)
        print ('yield异常2 L')
        
f=loopfun2(nested2)

print (next(f))




print('#############################################')


'''
x=0   
def dp2(s):

    global x
    x=x+1
    print('x:',x)
    
    if isinstance(s,(int,str)):
        print ('if1')
        print (s)
        print ('if2')
        print ('')
         
    else:
        print('else1')
        for item in s:
            print ('for1')
            print ('item:',item)
            dp2(item)
            print ('for2',item)
            print ('-------')
        print('else2')
        print ('++++++')


dp2(nested)

'''



print('#############################################')

'''
n=0
m=0
def dp(s):
    
    global  n
    global  m
    n=n+1
    print('n:',n)
    
    if isinstance(s,(int,str)):
        print ('if1:',s)
        m=m+1
        print('n:',n)
        #yield s
        print ('if2:',s)
        print ('')
        pass
    else:
        for item in s:
            
            print ('else1:',item)
            dp(item)
            
            print ('else2:',item)

            print ('else3:',item)
            print ('')
            yield s

a=dp(nested)

print(next(a))


'''
print('#############################################')






























        
