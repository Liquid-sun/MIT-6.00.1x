#!/usr/bin/env python

import math


def polysum(n, s):
    """Return a sum of a polygon area and square
       of the perimeter of the reqular polygon.

    Args:
      n (int): number of sides in the polygon
      s (float): length of each side of the polygon

    Returns:
      float, runded to 4

    Examples:
      >>> polysum(4, 4)

    """
    area = ((0.25*n*(s**2))/(math.tan(math.pi/n)))
    perimeter = n * s
    result = area + (perimeter**2)
    return round(result, 4)


if __name__==("__main__"):
    print polysum(5, 6)
    print polysum(10, 55)


