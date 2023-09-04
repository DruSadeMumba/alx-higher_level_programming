#!/usr/bin/python3
"""Addition of 2 ints or float"""


def add_integer(a, b=98):
    """add 2 ints/ floats"""
    for value, val in [("a", a), ("b", b)]:
        if not isinstance(val, (int, float)):
            raise TypeError("{} must be an integer".format(value))
    return int(a) + int(b)
