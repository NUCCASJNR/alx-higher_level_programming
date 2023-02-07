#!/usr/bin/python3

"""4-from_json_string.py module"""


import json
"""The json module"""


def from_json_string(my_str):
    """a function that returns an object (Python data structure)
    represented by a JSON string
    Arguments:
        my_str: the object to be returned
    """

    return json.loads(my_str)
