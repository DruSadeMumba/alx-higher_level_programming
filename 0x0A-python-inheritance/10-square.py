#!/usr/bin/python3
"""inherits from 9-rectangle.py"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from rectangle class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
