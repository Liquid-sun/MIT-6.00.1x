#!/usr/bin/env python

"""
Problem 7
(20 points possible)

Assume you are given two dictionaries d1 and d2, each with integer keys and integer values.
You are also given a function f, that takes in two integers, performs an unknown operation on them, and returns a value.

Write a function called dict_interdiff that takes in two dictionaries (d1 and d2).
The function will return a tuple of two dictionaries: a dictionary of the intersect of d1 and d2
and a dictionary of the difference of d1 and d2, calculated as follows:

intersect: 
The keys to the intersect dictionary are keys that are common in both d1 and d2. 
To get the values of the intersect dictionary, look at the common keys in d1 and d2
and apply the function f to these keys' values -- the value of the common key in d1
is the first parameter to the function and the value of the common key in d2 is 
the second parameter to the function. 
Do not implement f inside your dict_interdiff code -- assume it is defined outside.

difference:
a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears
only in d1 and not in d2 or (b) every key-value pair in d2 whose key appears only in d2 and not in d1.


"""

import itertools


def f(x, y):
    return x > y


def dict_interdiff(d1, d2):
    """
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above,
    
    """
    
    s1 = set(d1.keys())
    s2 = set(d2.keys())
    s1_out = s1.intersection(s2)
    
    d_out_1 = {k:f(d1[k], d2[k]) for k,v in d1.items() if k in s1_out}

    da = {k:v for k,v in d1.items() if k not in d2.keys()}
    db = {k:v for k,v in d2.items() if k not in d1.keys()}

    d_out_2 = dict(itertools.chain(da.items(), db.items()))

    return (d_out_1, d_out_2)



if __name__=="__main__":
   #d1 = {1:30, 2:20, 3:30, 5:80}
   #d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
   d1 = {1:30, 2:20, 3:30}
   d2 = {1:40, 2:50, 3:60}
   
   print dict_interdiff(d1, d2)    

