
def len_recur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr == '':
        return 0
    return 1 + lenRecur(aStr[1:])


print len_recur('Hello World')

