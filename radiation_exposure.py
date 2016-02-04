#!/usr/bin/env python



def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiation_exposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    exposure = stop - start
    steps = exposure / step
    area_total = 0
    
    while(steps > 0):
        area = f(start) * step
        area_total += area
        start += step
        steps -= 1
       
    return area_total

