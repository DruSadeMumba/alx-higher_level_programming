#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """class with public area method and integer_validator area"""
    def area(self):
        """this method is not defined"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this validates that value is int && > 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
