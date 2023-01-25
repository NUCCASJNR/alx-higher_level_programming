#!/usr/bin/python3
# 4-square.py by Al-Areef
"""A class that defines a square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing the square class
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Retrieves value of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Calculates the area of the square
        Returns: The square of the size
        """

        return self.__size ** 2
