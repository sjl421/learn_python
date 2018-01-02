'''map = str.maketrans('123','abc', '78')#要删除的字符需要在这指定
print (map)
s = '54321123789'
print (s.translate(map))'''

'''

def initdict(data):
    data['first']={}
    data['mid']={}
    data['last']={}
    return data
    

def showdict(data,label,name):
    return data[label].get(name)


def additem(data,fullname):
    splitname=fullname.split(' ')
    labels=['first','mid','last']
    if len(splitname)==2:
        print (splitname)
        splitname.insert(1,' ')
        print (splitname)
    for label,name in zip(labels,splitname):
        people=data[label].get(name)       
        if people:
            print('pass')
            data[label].setdefault(name,[]).append(fullname)
                
        else:
            data[label][name]=[fullname]

phonebook={}
initdict(phonebook)
additem(phonebook,'jack jr jason')
additem(phonebook,'tom jarry cidy')
additem(phonebook,'tom ha hade')
additem(phonebook,'tom hade')
print  (showdict(phonebook,'first','tom'))
'''


'''
phonebook={'first':{'ann':['tom jarry cidy']}}
phonebook['first'].setdefault('ann',[]).append('tom ha hade')
print (phonebook)
'''

'''
st={}
st['first']={}
st['mid']={}
st['last']={}

me='mag lie het'
st['first']['mag']=[me]
st['mid']['lie']=[me]
st['last']['het']=[me]
print (st['last']['het'])

mysister='an lie het'
st['first'].setdefault('an',[]).append(mysister)
st['mid'].setdefault('lie',[]).append(mysister)
st['last'].setdefault('het',[]).append(mysister)
print (st)
'''





def initdict(data):
    data['first']={}
    data['mid']={}
    data['last']={}
    return data
    

def showdict(data,label,name):
    return data[label].get(name)


def additem(data,fullname):
    splitname=fullname.split(' ')
    labels=['first','mid','last']
    if len(splitname)==2:
        print (splitname)
        splitname.insert(1,' ')
        print (splitname)
    for label,name in zip(labels,splitname):
        people=data[label].get(name)       
        if people:
            print('pass')
            people.append(fullname)
                
        else:
            data[label][name]=[fullname]

phonebook={}
initdict(phonebook)
additem(phonebook,'jack jr jason')
additem(phonebook,'tom jarry cidy')
additem(phonebook,'tom ha hade')
additem(phonebook,'tom hade')
print  (showdict(phonebook,'first','tom'))

