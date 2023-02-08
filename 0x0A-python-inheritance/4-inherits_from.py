#!/usr/bin/python3
"""This module contain an inherited class checking function"""


def inherits_from(obj, a_class):
    """
    Check if an object is an inherited instance of a class
    Arguments:
        obj (any): the object to be checked
        a_class (type): The class to match to
    Return:
        True or False
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
