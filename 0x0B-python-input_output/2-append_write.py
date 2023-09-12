#!/usr/bin/python3
"""Write a function that appends a string to a text file"""


def append_write(filename="", text=""):
    """add to text file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
