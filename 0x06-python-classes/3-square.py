#!/usr/bin/python3
# 3-square.py by Al-Areef
"""A class that defines a square"""


class Square:
    """Represents the square"""

    def __init__(self, size=0):
        """initializing the square class
        Args:
            size - Size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """

            calculatr area of the sqaure
            Returns: The square of the size
            """

        return (self.__size ** 2)
