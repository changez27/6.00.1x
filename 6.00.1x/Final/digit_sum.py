'''
Created on 06-Mar-2018

@author: Prateek
'''
def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    temp = list(s)
    count = 0
    rslt = 0
    for item in temp:
        try:    
            if (int(item) >= 0):
                count += 1
                rslt += int(item)            
        except:
            continue
    
    if count > 0:
        return rslt
    else:
        raise ValueError  
           
           
x = sum_digits("asdfgh0000jkl")
print(x)