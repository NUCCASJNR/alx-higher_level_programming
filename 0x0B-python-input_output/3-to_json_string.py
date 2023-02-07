#!/usr/bin/python3

"""3-to_json_string.py module"""


import json
"""takes any python data type and convert it to string representation"""


def to_json_string(my_obj):
    """Initializing the function
        return:
            json representation
    """

    return json.dumps(my_obj)
