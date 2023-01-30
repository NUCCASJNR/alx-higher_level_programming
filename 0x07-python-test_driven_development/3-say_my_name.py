#!/usr/bin/python3
"""A function that prints My name is <first name> <last name>
    Args:
        first_name: first Argument
        last_name: second Argument
        if type of first_name and last_name is not string
        raise TypeError("first_name must be a string)
        (or last_name must be a string")
"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is " + first_name, last_name)
