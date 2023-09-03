#!/usr/bin/python3
"""prints square with #"""


def print_square(size):
    """prints square with #"""
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print("#" * size)
