#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """ initializing the square class"""

    def __init__(self, size=0, position=(0, 0)):
        """create a square
        Args:
            size: length of the square
            position: position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Retrieves the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
             raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #
            if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            [print("") for a in range(self.__position[1])]
            for b in range(self.__size):
                for a in range(self.__position[0]):
                    print(" ", end="")
                for c in range(self.__size):
                    print("#", end="")
                print()


