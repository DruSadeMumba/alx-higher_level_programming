#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for x in matrix:
        sq = list(map(lambda i: i**2, x))
        sq_matrix.append(sq)
    return sq_matrix
