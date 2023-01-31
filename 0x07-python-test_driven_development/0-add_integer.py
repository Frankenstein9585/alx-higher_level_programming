#!/usr/bin/python3
"""Define a function add_integer()."""

def add_integer(a, b=98):
    """
    Return the integer addition of a and b
    
    Args:
        a (int): An integer
        b (int): An integer
    
    Float arguments are typecasted to ints before addition is performed

    Raises:
        TypeError: If either a or b is a non-integer or a non-float
    """
    if type(a) not in [float, int]:
        raise TypeError('a must be an integer')
    if type(b) not in [float, int]:
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
