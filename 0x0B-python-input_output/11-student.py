#!/usr/bin/python3
"""defines a student"""


class Student:
    """a student"""
    def __init__(self, first_name, last_name, age):
        """init student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict rep"""
        if type(attrs) is list and all(type(var) is str for var in attrs):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """replace all attributes"""
        for key, val in json.items():
            setattr(self, key, val)
