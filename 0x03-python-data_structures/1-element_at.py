#!/usr/bin/python3
def element_at(my_list, idx):
    x = len(my_list)
    if idx < 0 and idx >= x:
        return None
    return my_list[idx]
