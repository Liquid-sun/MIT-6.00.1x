#!/usr/bin/env python



def longestRun(L):
    max = 1
    c = 0
    for i in range(len(L)):
        try:
            if L[i] >= L[i-1]:
                c += 1
                if c > max:
                    max = c
            else:
                c = 1
        except IndexError:
            pass

    return max





if __name__=="__name__":
    L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]

    print longestRun(L)
