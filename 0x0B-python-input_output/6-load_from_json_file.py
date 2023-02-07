#!/usr/bin/python3

"""6-load_from_json_file.py module"""

import json
"""The json module"""


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”
    Arguments:
        filename: The file to be created from the json file
    """

    with open(filename, "r") as a:
        return json.load(a)
