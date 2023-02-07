#!/usr/bin/python3

"""9-student.py module"""


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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""

        return self.__dict__
