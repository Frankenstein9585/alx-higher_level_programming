#!/usr/bin/python3
"""Function to print a name"""


def say_my_name(first_name, last_name=""):
    """
    Prints a name

    Raises:
        TypeError: If either first_name or last_name is not a string
    """

    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
