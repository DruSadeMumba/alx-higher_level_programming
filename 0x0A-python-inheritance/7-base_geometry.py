#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """class with various methods"""
    def area(self):
        """not defined"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """int validator"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
