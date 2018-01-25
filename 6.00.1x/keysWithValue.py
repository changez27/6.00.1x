def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    l = []
    for k,v in aDict.items(): 
        if v == target:
            l.append(k)
            
    l.sort()
    return l

dic = {3:123, 5:456, 4:123, 2:123}
x = keysWithValue(dic, 248)
print (x)