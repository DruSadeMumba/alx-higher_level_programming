#!/usr/bin/python3
"""defines a rectange"""


class Rectangle:
    """reping a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @property
    def height(self):
        return self.height

    def set_att(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
        setattr(self, f"__{name}", value)

    @width.setter
    def width(self, value):
        self.set_att("width", value)

    @height.setter
    def height(self, value):
        self.set_att("height", value)
