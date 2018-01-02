#-*-coding:utf-8-*-
#冒泡排序
def maopao(L):
    c=len(L)
    flag=True
    for i in range(c):
        if flag==True:
            flag==False
            for j in range(c-2,i-1,-1):
                #print(j,j+1)
                #print(L[j],L[j+1])
                #print('----')
                if L[j]>L[j+1]:
                    L[j],L[j+1]= L[j+1],L[j]
                    flag=True
    return L

#简单选择排序
def xuanze(L):
    c=len(L)
    for i in range(c):
        min=i
        for j in range(i+1,c):
            #print(i,min,j)
            if L[min]>L[j]:
                min=j
        if min!=i:
            L[i],L[min]=L[min],L[i]
            #print('min=',str(min))
            #print('L[i]',str(L[i]))
            #print('-----')
    return L

#直接插入排序
def charu(L):
    c=len(L)
    for i in range(1,c):
        key=L[i]
        j=i-1
        while j>=0:
            if L[j]>key:
                L[j],L[j+1]=key,L[j]
            j-=1
    return L

def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        print('key',str(key))
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                #lists[j + 1] = lists[j]
                #lists[j] = key
                lists[j + 1], lists[j]=lists[j], key
            j -= 1
            print(lists)
            print(j)
        print('--')
    return lists    

l=[10,9,8,7,6,5,4,3,2,1]
print(charu(l))



    



