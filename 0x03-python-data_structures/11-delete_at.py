#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    x = len(my_list)
    if idx < 0 or idx >= x:
        return my_list
    else:
        for i in range(x):
            del my_list[:idx]
            return my_list
