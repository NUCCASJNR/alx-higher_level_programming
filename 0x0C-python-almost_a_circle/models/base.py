#!/usr/bin/python3

"""The base.py module"""


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
