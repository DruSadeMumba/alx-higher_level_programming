#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    x = len(new) + 1
    result = 0
    for i in range(x):
        result += i
    return result
