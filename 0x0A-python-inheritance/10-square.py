#!/usr/bin/python3

"""inherits from baseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The square class is a sub class of the rectangle class
    It has the following private attribute:
        size = size
        It inherits the integer validator from the rectangle class
    """

    def __init__(self, size):
        """Validates the size attribute"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the string representation"""

        return str("[Rectangle] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Returns the area of the square"""

        return self.__size ** 2
