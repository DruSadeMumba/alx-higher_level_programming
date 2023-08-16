#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or my_list == '':
        return 0

    sums, div = 0, 0
    for i in my_list:
        x, y = i[0], i[1]
        sums += x * y
        div += y
    return sums / div
