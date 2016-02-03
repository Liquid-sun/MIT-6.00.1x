#!/usr/bin/env python

"""

Write a function called ndigits, that takes
an integer x (either positive or negative) 
as an argument. This function should return 
the number of digits in x.

"""

def ndigits(x):
    s = str(x).strip('-')
    if s != "":
        return 1 + ndigits(s[1:])
    else:
        return 0


