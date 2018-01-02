# -*- coding: cp936 -*-
import re

def ConvetToDMS(value):

    if re.match(r'[0-9]+\.\d{6}', str(value)) and len(str(value))<11:

        value=float(value)
        L = str(value).split('.')
        DD = L[0]
        
        tempMM = (value-int(L[0]))*60
        MM = str(tempMM).split('.')[0]
        
        SS = str((tempMM-int(MM))*60).split('.')[0]
        
        res = DD+'.'+MM+'.'+SS

        return res
    
    else:
        print('请输入正确的10进制坐标!')


def ConvetToDecimalism(value):
    
    if re.match(r'\d{1,3}\.\d{2}\.\d{2}',value):

        L=str(value).split('.')
        M1=int(L[0])
        M2=float(L[1])/60
        M3=float(L[2])/3600   
        res=(M1+M2+M3)
        
        return round(res,6)
    else:
         print('请输入正确的60进制坐标!')
        


def OutPutRes(value,type=0):
    if type==1:
        print ('GPS坐标: %s 转换为: %s'%(value,ConvetToDecimalism(value)))
    else:
        print ('GPS坐标: %s 转换为: %s'%(value,ConvetToDMS(value)))



OutPutRes('39.928902')
OutPutRes('30.55.44',1)











