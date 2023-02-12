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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        file_name = "{}.json".format(cls.__name__)
        with (open(file_name, "w")) as a:
            if list_objs is None or list_objs == []:
                a.write("[]")
            else:
                list_dict = [i.to_dictionary() for i in list_objs]
                a.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""

        if json_string is None or json_string == []:
            return ("[]")
        return (json.loads(json_string))
