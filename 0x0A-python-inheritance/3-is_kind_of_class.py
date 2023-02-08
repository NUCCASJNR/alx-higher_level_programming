#!/usr/bin/python3

""""a function that returns True if the object is exactly an
instance of the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """Defining the function"""

    if type(obj) == a_class or isinstance(obj, a_class):
        return (True)
    else:
        return (False)
