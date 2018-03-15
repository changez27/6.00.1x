'''
Created on 06-Mar-2018

@author: Prateek
'''

def primes_list(N):
    '''
    N: an integer
    '''
    if N < 2:
        return []
    elif N == 2:
        return [2]
    else:
        list = [2]
        for n in range(3,N+1):
            flag = 0
            for div in range(2,int(n/2)+1):
                if (n % div == 0):
                    print(n)
                    flag = 1
                    break
            if flag == 0:
                list.append(n)
        return list

x = primes_list(100)
print(x)