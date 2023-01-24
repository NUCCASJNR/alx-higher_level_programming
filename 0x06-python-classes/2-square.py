#!/usr/bin/python3
# 2-square.py written by Al-Areef

class Square:
    """Represents the square"""

    def __init__(self, size=0):
        """initializing the square class
        size- size of the square

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
