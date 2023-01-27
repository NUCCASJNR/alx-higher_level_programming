#!/usr/bin/python3
""" function that adds 2 integers."""


def add_integer(a, b=98):
    """Adds int a & b """
    if not isinstance(a, int) | isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) | isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
