#!/usr/bin/python3

def print_last_digit(number):
    x = number % 10
    if number < 0:
        x = -number % 10
    print('{}'.format(x), end='')
    return x
