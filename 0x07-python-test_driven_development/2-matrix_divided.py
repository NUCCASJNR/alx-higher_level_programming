#!/usr/bin/python3
""" a function that divides all elements of a matrix."""

def matrix_divided(matrix, div):
    if isinstance(matrix, list(int)) | isinstance(matrix, list(float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif len(matrix) == 
