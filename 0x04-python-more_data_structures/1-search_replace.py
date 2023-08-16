#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    x = len(new)
    for i in range(x):
        if new[i] == search:
            new[i] = replace
    return new
