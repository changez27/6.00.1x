def sumDigits(N):
    '''
    Return the sum of digits of the given number.
    
    N: a non-negative integer
    '''
    sum = N%10
    if N//10 == 0:
        return N
    else:
        return sum + sumDigits(N//10)