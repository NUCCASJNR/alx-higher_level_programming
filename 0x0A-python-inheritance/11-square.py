#!/usr/bin/python3
"""This module contain the class Square inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The subclass Square inheriting from rectangle"""
    def __init__(self, size):
        """The initializer function"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
