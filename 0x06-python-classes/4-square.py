#!/usr/bin/python3
"""defines a square"""


class Square:
    """square with private instance attribute: size"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be an integer")

    def area(self):
        area = self.__size ** 2
        return area
