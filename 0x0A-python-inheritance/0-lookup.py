#!/usr/bin/python3
"""
A function that return the list of available
attributes and methods of an object
"""


def lookup(obj):
    """list of attr"""
    return dir(obj)
