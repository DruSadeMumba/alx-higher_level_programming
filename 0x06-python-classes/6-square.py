#!/usr/bin/python3
"""defines a square"""


class Square:
    """square with private instance attribute: size"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(val, int) for val in value) \
                or not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        area = self.__size ** 2
        return area

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end='')
            for i in range(self.__size):
                print("\n".join([" " * self.__position[0] +
                                 "#" * self.__size]))
