#!/usr/bin/python3

"""a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)"""

class Rectangle:
    """The Rectangle class"""

    def __init__(self, width=0, height=0):
    """Initializing the rectangle
       Args:
            width: width of the rectangle
            height: height of the rectangle
       Raises:
            TypeError: if width is not an integer
            ValueError: if width is < 0
    """
    self.width = width
    self.height = height

    @property
    def width(self):
        """Retrieves the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Sets the height"""
        
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        rett
