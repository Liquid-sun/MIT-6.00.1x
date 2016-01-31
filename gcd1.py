

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = 1
    for i in range(1, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            if i > gcd:
                gcd = i
    return gcd

if __name__=="__main__":
    print(gcdIter(4,20))

