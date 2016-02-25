#!/usr/bin/env python

import math


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<{}, {}>".format(self.x, self.y)

    def distance(self, other):
        return math.sqrt(pow((self.x - other.x), 2)
            + pow((self.y - other.y), 2))




if __name__=="__main__":
    c1 = Coordinate(4,5)
    print c1
    c2 = Coordinate(2,3)
    print c2

    print c1.distance(c2)


