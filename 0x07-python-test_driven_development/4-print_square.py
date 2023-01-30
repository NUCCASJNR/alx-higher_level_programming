#!/usr/bin/python3

"""a function that prints a square with the character #.
    Args:
        size: length of the square
        Raise: TypeError if size isnt an integeger
               ValueError if size is less than 0
               TypeError if size is a float and is less than 0
"""


def print_square(size):
    """size: length of the square"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and type(size) < 0:
        raise TypeError("size must be an integer")
    for a in range(size):
        for b in range(size):
            print("#", end="")
        print()
