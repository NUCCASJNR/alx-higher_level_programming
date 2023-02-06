#!/usr/bin/python3

"""6-base_geometry.py module"""


class BaseGeometry:
    """The BaseGeometry class"""

    def area(self):
        """Initializing the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Initializing"""

        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
