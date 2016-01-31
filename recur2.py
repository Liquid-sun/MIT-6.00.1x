

def recurPowerNew(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    """
    if exp == 0:
        return 1
    if exp%2 != 0:
        return base * recurPowerNew(base, exp-1)
    if exp%2 == 0:
        return recurPowerNew(base*base, exp/2)


if __name__=="__main__":
    print "Even: ", recurPowerNew(2,4)
    print "Odd: ", recurPowerNew(2,5)
    print "Zero: ", recurPowerNew(2, 0)


    
