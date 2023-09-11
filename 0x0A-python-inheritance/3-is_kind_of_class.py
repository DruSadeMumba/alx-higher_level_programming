#!/usr/bin/python3
"""Write a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class
"""


def is_kind_of_class(obj, a_class):
    """obj and a_class are same or instance of"""
    return isinstance(obj, a_class)
