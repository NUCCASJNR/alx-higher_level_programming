#!/usr/bin/python3

"""inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class to define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Istantiation
            Validates the following attributes:
                - width
                - height

        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Returns the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the object"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
