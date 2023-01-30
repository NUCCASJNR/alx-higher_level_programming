#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """Represents a Rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing the Rectangle class
            Args:
                width: width ofthe rectangle
                height: height of the rectangle
            Raises:
                TypeError: if width of the rectangle
                ValueError: if widthis < 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
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
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a rectangle"""

        if self.__height == 0 or self.__width == 0:
            return ("")
        Rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    Rectangle += str(self.print_symbol)
                except Exception:
                    Rectangle += type((self).print_symbol)
            if i < self.__height - 1:
                Rectangle += "\n"
        return Rectangle

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of the rectangle"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
