#!/usr/bin/python3
"""divides all elements"""


def matrix_divided(matrix, div):
    """division of matrix"""
    if not all(isinstance(row, list)
               and all(isinstance(i, (int, float)) for i in row)
               for row in matrix) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in row] for row in matrix]
