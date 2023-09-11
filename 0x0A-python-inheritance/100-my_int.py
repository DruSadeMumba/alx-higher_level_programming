#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """rebel class"""

    def __eq__(self, other):
        return self.real != other

    def __ne__(self, other):
        return self.real == other
