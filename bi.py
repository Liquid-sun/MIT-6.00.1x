
def findRoot(x, power, epsilon):
    if x < 0 and power*2 == 0:
        return None

    low = min(0, x)
    high = max(0, x)
    ans = (high+low)
