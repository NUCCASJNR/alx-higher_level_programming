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
        """Retrieves the height"""

        return self.__height

    @height.setter
    def height(self, value):
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
        else:
            return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """Returns a rectangle"""

        if self.__height == 0 or self.__width == 0:
            return ""
        Rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                Rectangle += "#"
            if i < self.__height - 1:
                Rectangle += "\n"
        return Rectangle

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
