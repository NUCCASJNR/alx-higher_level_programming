#!/usr/bin/python3

"""A class that defines a rectangle based on 0-rectangle.py"""


class Rectangle:
    """Represents the square"""

    def __init__(self, width=0, height=0):
        """Initializing the Rectangle class
            Args:
                width: width of the rectangle
                height: height of the rectangle
            Raises:
                TypeError: if width is not an integer
                ValueError: if width is < 0
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieves the width of the  rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
