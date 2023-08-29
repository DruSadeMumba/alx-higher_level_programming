#!/usr/bin/python3
"""Python class MagicClass"""
import math


class MagicClass:
    """Circle Magic Class"""
    def __init__(self, radius=0):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return self.__radius * 2 * math.pi
