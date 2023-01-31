#!/usr/bin/python3
"""Define a function to divide a matrix"""


def matrix_divided(matrix, div):
    """
    Return the division of the values in a matrix

    Args:
        matrix (list of lists): containing numbers to be divided
        div (int or float): the divisor

    Raises:
    TypeError: If div is not a number
    TypeError: If the lists in the matrix are of different sizes
    TypeError: If the elements in the lists are not numbers
    ZeroDivisionError: If div is 0
    """

    new_matrix = list()
    new_row = list()
    size = len(matrix[0])
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        if len(row) != size:
            raise TypeError('Each row of the matrix must have the same size')
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        new_row = [round(i / div, 2) for i in row]
        new_matrix.append(new_row)
    return new_matrix
