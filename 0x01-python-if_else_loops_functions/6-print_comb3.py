#!/usr/bin/python3

for i in range(8):
    for j in range(10):
        if i != j and i < j:
            print('{}{}'.format(i, j), end=", ")
print('{}'.format(89))
