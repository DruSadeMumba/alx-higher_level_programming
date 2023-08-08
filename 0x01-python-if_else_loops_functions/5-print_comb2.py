#!/usr/bin/python3

for numbers in range(10):
    print(f'{0}{numbers:d}', end=", ")
print(*range(10, 100), sep=", ")
