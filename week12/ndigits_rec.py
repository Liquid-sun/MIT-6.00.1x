#!/usr/bin/env python

"""

Write a function called ndigits, that takes
an integer x (either positive or negative) 
as an argument. This function should return 
the number of digits in x.

"""


def ndigits(x):
    """Return a number (int) of digits in the given x.

    Args:
      x (int): negative or positive

    """
    s = str(x).strip('-')         # change int to str and strip leading '-'
    if s != "":                   # string not empty - apply func to str = str - 1st digit
        return 1 + ndigits(s[1:])
    else:
        return 0                  # string is empty, finish counting




