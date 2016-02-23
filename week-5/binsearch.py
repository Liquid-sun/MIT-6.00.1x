#!/usr/bin/env python

"""

Binary search with recursive calls.

"""


def search(L, e):
    """
    Args:
      L: list
      e: element in a list that we search for

    """
    def bSearch(L, e, low, high):
        if high == low:
            return L[low] == e
        
        mid = low + int((high - low)/2)
        
        if L[mid] == e:
            return True
        if L[mid] > e:
            return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)


