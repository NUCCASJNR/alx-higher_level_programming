#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[i * i for i in row] for row in matrix]
    return new
