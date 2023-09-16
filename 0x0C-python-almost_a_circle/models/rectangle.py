#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


def validate(val, name, min=None):
    """func to validate values"""
    if type(val) is not int:
        raise TypeError(f"{name} must be an integer")
    if min == 0 and val < min:
        raise ValueError(f"{name} must be >= {min}")
    if min == 1 and val < min:
        raise ValueError(f"{name} must be > 0")


class Rectangle(Base):
    """Rectangle class"""
    order = ['id', 'width', 'height', 'x', 'y']

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        validate(val, "width", 1)
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        validate(val, "height", 1)
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        validate(val, "x", 0)
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        validate(val, "y", 0)
        self.__y = val

    def area(self):
        """area of rect"""
        return self.__width * self.__height

    def display(self):
        """print rect inst with #"""
        if self.__width == 0 or self.__height == 0:
            print("")
        print("\n" * self.y +
              "\n".join(" " * self.__x +
                        "#" * self.__width for _ in range(self.__height)))

    def __str__(self):
        """str rep of rect"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} " \
               f"- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        if args:
            for attr, val in zip(self.order, args):
                setattr(self, attr, val)

        if kwargs:
            for attr, val in kwargs.items():
                setattr(self, attr, val)
