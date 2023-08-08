#!/usr/bin/python3

def fizzbuzz():
    for numbers in range(1, 101):
        if (numbers % 15 == 0):
            print('{}'.format("FizzBuzz"), end=" ")
        elif (numbers % 5 == 0):
            print('{}'.format("Buzz"), end=" ")
        elif (numbers % 3 == 0):
            print('{}'.format("Fizz"), end=" ")
        else:
            print('{}'.format(numbers), end=" ")
