#!/usr/bin/python3

"""10-student.py module"""


class Student:
    """The student class
        Args:
            first_name: 1st argument
            last_name: 2nd argument
            age: 3rd argument
    """

    def __init__(self, first_name, last_name, age):
        """Initializing a new Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""

        my_dict = dict()
        if type(attrs) is list and all(type(a) is str for a in attrs):
            for a in attrs:
                if a in self.__dict__:
                    my_dict.update({a: self.__dict__[a]})
            return my_dict

        return self.__dict__
