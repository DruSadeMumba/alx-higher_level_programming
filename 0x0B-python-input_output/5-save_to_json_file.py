#!/usr/bin/python3
"""Write a function that writes an Obj to a txt file, using a JSON rep"""
import json


def save_to_json_file(my_obj, filename):
    """json to file"""
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
