#!/usr/bin/python3

def magic_calculation(a, b, c):
    d = a + b
    e = a * b
    if a < b:
        return c
    elif b < c:
        return d
    else:
        return e - c
