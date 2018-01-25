def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """
    return f
def f(x):
    sum = 0
    exponent = len(L) - 1
    for y in L:
        sum = sum + y*(x**exponent)
        exponent -= 1
    return sum    
    
L = [1,2,3,4]        
x = general_poly(L)(2)
print(x)