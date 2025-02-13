"""
triangle functions
"""
__author__ = "Dominik Rohal"
__version__ = "1.0.0"

import math


def hypotenuse(a, b):
    """Returns the length of the hypotenuse when given the lengths of two other sides of a right-angled triangle"""
    return math.hypot(a,b)

def area(a, b):
    """returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters"""
    return a * b / 2