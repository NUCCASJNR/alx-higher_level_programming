#!/usr/bin/python3

"""The rectangle.py module"""

from models.base import Base


class Rectangle(Base):
    """The rectangle class that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the function
            creating an instance of the rectangle
            Args:
                width - width of the rectangle
                height - height of the rectangle
                x - 0
                y - 0
                id - None
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute"""

        return self.__width

    @property
    def height(self):
        """Retrieves the height attribute"""

        return self.__height

    @property
    def x(self):
        """Retrieves the x attribute"""
        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute"""

        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    
    @height.setter
    def height(self, value):
        """Sets the height attribute."""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets x attribute"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets y attribute"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
