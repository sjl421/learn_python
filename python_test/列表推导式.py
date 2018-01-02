#矩阵转换
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]

#1、循环方法
X=[]
for i in range(4):
    Y=[]
    for a in matrix:
        Y.append(a[i])
    X.append(Y)

print(X)

#2、推导式方法
print( [ [a[i] for a in matrix] for i in range(4)] )


print(list(zip(*matrix)))



# 一个由男人列表和女人列表组成的嵌套列表,取出姓名中带有两个以上字母e的姓名，组成列表
names = [['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'], 
         ['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']]


#1、递归循环实现

def qt(L):
     new=[]
     
     def js(L):
          
          if isinstance(L, (int, str)):
               if L.count('e') >= 2:
                   nonlocal new   #声明修改嵌套的外层变量
                   new.append(L)
          else:
               for d in L:
                    js(d)

     js(L)
     
     return new
               

print(qt(names))

#2、推导式实现

print ( [name for lst in names for name in lst if name.count('e') >= 2])



