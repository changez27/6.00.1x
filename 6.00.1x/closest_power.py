from builtins import int
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exponent = 0
    result = None
    dic = {}
    while True:
        power = base**exponent
        difference = abs(num - power)
        dic.update({difference:exponent})
        if power > num:
            break
        else:
            exponent += 1
    result = min(dic.keys())
    if type(num) == int:
        return dic[result]
    else:
        return dic[result] - 1
x = closest_power(12,100)
print(x)