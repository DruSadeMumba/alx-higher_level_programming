#!/usr/bin/python3
"""Write a class LockedClass with no class or object attribute"""


def LockedClass():
    """new instance attribute is called first_name."""
    __slots__ = ["first_name"]
