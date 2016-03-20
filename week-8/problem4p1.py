#!/usr/bin/env python


def getSublist(L, n):
    l = []
    
    for i in range(len(L)-n+1):
        l.append(L[0+i:n+i])
    
    return l

