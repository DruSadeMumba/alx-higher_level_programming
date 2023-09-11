#!/usr/bin/python3
"""Add new attr to an obj"""


def add_attribute(obj, att, val):
    """add attr to obj"""
    if hasattr(obj, '__dict__'):
        setattr(obj, att, val)
    else:
        raise TypeError("can't add new attribute")
