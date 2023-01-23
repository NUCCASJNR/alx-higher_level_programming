#!/usr/bin/python3

"""
a function that prints an integer with "{:d}".format().
Prototype: def safe_print_integer(value):
value can be any type (integer, string, etc.)
The integer should be printed followed by a new line
Returns True if value has been correctly printed
(it means the value is an integer)
Otherwise, returns False
You have to use try: / except:
You have to use "{:d}".format() to print as integer
You are not allowed to import any module
You are not allowed to use type()
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
