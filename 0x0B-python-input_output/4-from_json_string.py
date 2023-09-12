#!/usr/bin/python3
"""Write a function that returns an object reped by a JSON str"""
import json


def from_json_string(my_str):
    """from json-str"""
    return json.loads(my_str)
