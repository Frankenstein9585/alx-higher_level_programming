#!/usr/bin/python3
"""Function that prints a square"""


def print_square(size):
    """
    Prints a square.

    Args:
    size (int): Size of the square

    Raises:
        TypeError: If size is a non-integer
        ValueError: If size is less than 0
    """

    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        print(size * '#')
