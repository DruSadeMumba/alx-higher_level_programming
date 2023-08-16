#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for key, value in new.items():
        new.update({key: (value * 2)})
    return new
