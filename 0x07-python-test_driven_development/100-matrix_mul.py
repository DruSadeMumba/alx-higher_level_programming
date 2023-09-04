#!/usr/bin/python3
"""Multiply 2 matrices"""


def matrix_mul(m_a, m_b):
    """Multiply 2 matrices"""
    colA, colB = len(m_a[0]), len(m_b[0])
    rowA, rowB = len(m_a), len(m_b)
    variables = {"m_a": m_a, "m_b": m_b}

    for pos, val in variables.items():
        if not isinstance(val, list):
            raise TypeError(f"{pos} must be a list")

    for pos, val in variables.items():
        if not all(isinstance(row, list) for row in val):
            raise TypeError(f"{pos} must be a list of lists")

    for value, val in variables.items():
        if val == [] or val == [[]]:
            raise TypeError(f"{value} can't be empty")

    for item, val in variables.items():
        if not all(isinstance(value, (int, float))
                   for row in val for value in row):
            raise TypeError(f"{item} should contain only integers or floats")

    for items, val in variables.items():
        if not all(len(row) == len(val[0]) for row in val):
            raise TypeError(f"each row of {items} must be of the same size")

    if colA != rowB:
        raise ValueError("m_a and m_b can't be multiplied")

    new = [[sum(m_a[i][k] * m_b[k][j] for k in range(colB))
            for j in range(colB)] for i in range(rowA)]

    return new
