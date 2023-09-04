#!/usr/bin/python3
"""The N queens puzzle"""
from sys import *


def is_valid(args):
    if len(args) != 2:
        print("Usage: nqueens N")
        return False
    if not args[1].isdigit():
        print("N must be a number")
        return False
    return True


def _init(n):
    return [[i, None] for i in range(n)]


def in_pos(board, y):
    return any(row[1] == y for row in board)


def decline(board, x, y):
    return not any(
        in_pos(board, y) or abs(board[i][1] - y) == abs(i - x)
        for i in range(x)
    )


def clean(board, x):
    [board[i].__setitem__(1, None) for i in range(x, len(board))]


def _recurs(board, x):
    n = len(board)
    for y in range(n):
        clean(board, x)
        if decline(board, x, y):
            board[x][1] = y
            if x < n - 1:
                _recurs(board, x + 1)
            else:
                print(board)


if __name__ == "__main__":
    if is_valid(argv):
        n = int(argv[1])
        if n < 4:
            print("N must be at least 4")
        else:
            board = _init(n)
            _recurs(board, 0)
