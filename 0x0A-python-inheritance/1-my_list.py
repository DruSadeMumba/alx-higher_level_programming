#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """inherit class list"""
    def __int__(self):
        """initiate super class"""
        super().__init__()

    def print_sorted(self):
        """print sorted"""
        print(sorted(self))
