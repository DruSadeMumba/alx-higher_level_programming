#!/usr/bin/python3

for numbers in range(100):
    if numbers < 10:
        print(f'{0}{numbers:d}', end=", ")
    elif numbers < 99:
        print(f'{numbers:d}', end=", ")
    else:
        print('{}'.format(numbers))
