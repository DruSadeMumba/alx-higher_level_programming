#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = len(my_list)
    if idx < 0 or idx >= x:
        return None
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
