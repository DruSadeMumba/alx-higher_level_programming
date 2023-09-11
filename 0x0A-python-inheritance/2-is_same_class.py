#!/usr/bin/python3
"""
A function that return True if the object is
exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """are obj and a_class same"""
    if type(obj) == a_class:
        return True
    return False
