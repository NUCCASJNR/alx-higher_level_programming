#!/usr/bin/python3

"""The base.py module"""
import json


class Base:
    """"The base class for all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The initialization function
           Args:
                id: None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json string representation"""

        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))
