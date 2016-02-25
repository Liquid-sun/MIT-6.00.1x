#!/usr/bin/env python

"""
Your task is to define the following two methods for the Coordinate class:

Add an __eq__ method that returns True if coordinates refer
to same point in the plane (i.e., have the same x and y coordinate).

Define __repr__, a special method that returns a string that looks 
like a valid Python expression that could be used to recreate 
an object with the same value. 
In other words, eval(repr(c)) == c given the definition of __eq__ from part 1.

"""



class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing
        # an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __repr__(self):
        return "Coordinate({}, {})".format(self.x, self.y)



def main():
    pass


if __name__=="__main__":
   c1 = Coordinate(3,4)
   c2 = Coordinate(6,4)
   print("c1 == c2 ? {}".format(c1 == c2))
   print repr(c2)


