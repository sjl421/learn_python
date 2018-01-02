print('')
print('1、阶乘')
def factorial(n):
     if n==1:
          return 1
     else:
          return n*factorial(n-1)
print(factorial(5))


def fb(n):
     a=[0,1]
     for i in range(n-2):
          a.append(a[-1]+a[-2])
     print (a)
fb(5)



print('')
print('2、幂次方')

def pow(x,y):
    if y==1:
        return x
    else:
        return x*pow(x,y-1)
    
print (pow(10,3))


def pow2(x,y):
    res=1
    for i in range(y):
        res = res * x
    return res

print (pow2(2,3))


print('')
print('3、折半查找')


def serch(seq,number,lower=0,upper=None):
    if upper is None:
        upper=len(seq)-1
    if lower==upper:
        assert number==seq[upper]
        return upper
    else:
        middle=(lower+upper)//2
        if number>seq[middle]:
            return serch(seq,number,middle+1,upper)
            
        else:
            return serch(seq,number,lower,middle)
        

seq=[3,4,1,7,5,8,3,2]
seq.sort()
print(seq)
print(serch(seq,8))

