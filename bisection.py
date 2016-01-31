

def find_root(x, power, epsilon):
    low = 0
    high = x
    ans = (high+low)/2.0

    while abs(ans**power-x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
    return ans


def find_root2(x, power, epsilon):
    if x < 0 and power%2 == 0:
        return None

    low = min(0, x)
    high = max(0, x)
    ans = (high+low)/2.0

    while abs(ans**power-x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
    return ans




if __name__=="__main__":
    print find_root(27.0, 3, 0.001)
    print find_root2(-27.0, 3, 0.001)



