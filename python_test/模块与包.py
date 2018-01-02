import sys,pprint,os
sys.path.append(r'C:\Users\liangrui\Desktop\py')
pprint.pprint(sys.path)
import copy
import http.client

pprint.pprint(dir(copy)) #获取所有特性
pprint.pprint (copy.__all__) #获取模块公有接口

print(help(copy.copy))#获取帮助

print(copy.__file__)#获取模块位置
print(http.client.__file__)



