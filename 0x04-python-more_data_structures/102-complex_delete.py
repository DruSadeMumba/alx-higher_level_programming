#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value:
        return a_dictionary
    key_del = list(a_dictionary.keys())
    for val in key_del:
        if value == a_dictionary.get(val):
            del a_dictionary[val]
    return a_dictionary
