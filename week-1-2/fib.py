

def fib(x):
    """Assume x is int >= 0 returns Fib of x"""
    assert type(x) == int and x >= 0
    if x in (0,1):
        return 1
    else:
        return fib(x-1) + fib(x-2)


if __name__=="__main__":
    print fib(5)

