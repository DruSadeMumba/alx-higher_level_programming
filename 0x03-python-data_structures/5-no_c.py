#!/usr/bin/python3
def no_c(my_string):
    for c in my_string:
        if ord(c) == 67 or ord(c) == 99:
            return my_string.translate({ord(c): None})
        return my_string
