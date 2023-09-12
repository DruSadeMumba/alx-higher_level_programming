#!/usr/bin/python3
"""
Create a function that returns a list of lists
of integers representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """pascal triangle"""
    if n <= 0:
        return []
    tri = [[1]]
    for i in range(n-1):
        tri.append([a + b for a, b in
                    zip([0] + tri[-1], tri[-1] + [0])])
    return tri
