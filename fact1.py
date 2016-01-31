
def fact_t(n):
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res


def fact_r(n):
    if n == 1:
        return n
    return n * fact_r(n-1)


if __name__=="__main__":
    print fact_t(10)
    print fact_r(10)

