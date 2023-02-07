#!/usr/bin/python3

"""5-save_to_json_file.py module"""

import json
"""The json module"""


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
    using a JSON representation
    Args:
        my_obj - the json representation
        filename - The file to be written into
    """

    with open(filename, "w+") as a:
        json.dump(my_obj, a)
