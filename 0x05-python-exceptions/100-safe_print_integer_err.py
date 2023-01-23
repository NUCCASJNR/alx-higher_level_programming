#!/usr/bin/python3

"""
Write a function that executes a function safely.

Prototype: def safe_function(fct, *args):
You can assume fct will be always a pointer to a function
Returns the result of the function,
Otherwise, returns None if something happens during the function
and prints in stderr the error precede by Exception:
You have to use try: / except:
"""


import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        return True
