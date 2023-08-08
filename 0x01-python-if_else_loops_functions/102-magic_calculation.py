#!/usr/bin/python3

def magic_calculation(a, b, c):
    d = a + b
    e = d - c
    if a < b:
        return c
    elif c > b:
        return d
    else:
        return e
