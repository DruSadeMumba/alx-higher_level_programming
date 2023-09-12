#!/usr/bin/python3
"""
Write a script that adds all args to a PyList, and then save them to a file
"""
from sys import *
Save = __import__('5-save_to_json_file').save_to_json_file
Load = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        items = Load("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(argv[1:])
    Save(items, "add_item.json")
