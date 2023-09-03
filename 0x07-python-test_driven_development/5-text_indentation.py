#!/usr/bin/python3
"""print 2 lines after char"""


def text_indentation(text):
    """Write a function that prints a text with 2 new"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delim = ['.', '?', ':']
    sentence = ""

    for char in text:
        sentence += char
        if char in delim:
            print(sentence)
            print("")
            sentence = ""

    if sentence:
        print(sentence, end="")
