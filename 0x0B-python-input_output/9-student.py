#!/usr/bin/python3
"""defines a student"""


class Student:
    """a student"""
    def __init__(self, first_name, last_name, age):
        """init student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict rep"""
        return self.__dict__
