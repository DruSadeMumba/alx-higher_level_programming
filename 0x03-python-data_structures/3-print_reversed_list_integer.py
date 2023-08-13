#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = len(my_list)
    for i in reversed(range(x)):
        print('{:d}'.format(my_list[i]))
