#!/usr/bin/python3
"""print my name"""


def say_my_name(first_name, last_name=""):
    """print my name"""
    for name, val in [("first_name", first_name),
                      ("last_name", last_name)]:
        if not isinstance(val, str):
            raise TypeError("{} must be a string".format(name))
    print('My name is {} {}'.format(first_name, last_name))
