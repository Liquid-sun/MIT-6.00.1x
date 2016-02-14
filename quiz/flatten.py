#!/usr/bin/env python

"""
Problem 6
(15 points possible)

Write a function to flatten a list. The list contains other lists, strings, or ints.
For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] 

"""


def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flt = lambda *n: (e for a in n for e in (flt(*a) if isinstance(a, list) else (a,)))
    return list(flt(aList))


if __name__=="__main__":
    test_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    flat = flatten(test_list)
    print flat

