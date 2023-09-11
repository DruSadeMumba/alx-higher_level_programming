#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """inherit class list"""
    def __init__(self):
        """initiate super class"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
