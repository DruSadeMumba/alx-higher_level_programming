#!/usr/bin/python3
"""defines a square"""

class Square:
    """square with private size attribute"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")