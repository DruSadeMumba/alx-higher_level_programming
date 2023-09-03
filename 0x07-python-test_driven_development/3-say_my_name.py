#!/usr/bin/python3
"""print my name"""


def say_my_name(first_name, last_name=""):
    """print my name"""
    for name, val in [("first_name", first_name),
                      ("last_name", last_name)]:
        if not isinstance(val, str):
            raise TypeError(f"{name} must be a string")
    print('My name is {} {}'.format(first_name, last_name))
