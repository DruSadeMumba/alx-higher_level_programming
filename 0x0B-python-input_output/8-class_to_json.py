#!/usr/bin/python3
"""
Write a function that returns the dict desc with simple
data struct for JSON serialization of an obj
"""


def class_to_json(obj):
    """dict rep"""
    return obj.__dict__
