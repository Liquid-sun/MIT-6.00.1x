


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    res = 1
    while(exp > 0):
        res = res * base
        exp -= 1
    return res

if __name__=="__main__": 
    iterPower(2, 4)
