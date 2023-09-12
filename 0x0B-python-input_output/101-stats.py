#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics"""
from sys import *


def print_stats(size, codes):
    """print the stats"""
    print(f'File size: {size}')
    for key, val in sorted(codes.items()):
        print(f'{key}: {val}')


if __name__ == "__main__":
    """main func"""
    size = 0
    count = 0
    codes = {"200": 0, "301": 0,
             "400": 0, "401": 0,
             "403": 0, "404": 0,
             "405": 0, "500": 0}

    try:
        for line in stdin:
            modline = list(map(str, line.strip().split(" ")))
            size += int(modline[-1])
            if modline[-2] in codes:
                codes[modline[-2]] += 1
            count += 1
            if count % 10 == 0:
                print_stats(size, codes)
    except KeyboardInterrupt:
        print_stats(size, codes)
        raise

    print_stats(size, codes)
