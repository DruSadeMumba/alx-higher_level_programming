#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul
    
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    
    sign = sys.argv[2]
    signs = {'+': add, '-': sub, '*': mul, '/': div}
    if sign not in list(signs.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
   
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sign == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif sign == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif sign == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    else:
        print('{} / {} = {}'.format(a, b, div(a, b)))
