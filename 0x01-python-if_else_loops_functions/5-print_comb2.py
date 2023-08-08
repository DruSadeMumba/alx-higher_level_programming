#!/usr/bin/python3

for numbers in range(10):
    print('{}{}'.format(0, numbers), end=", ")
print(*range(10, 100), sep=", ")
