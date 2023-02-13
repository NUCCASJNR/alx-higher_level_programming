#!/usr/bin/python3
"""This module contains the Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """The initialization function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the str representation"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

    @property
    def size(self):
        """Return the square size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Sef the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and len(args) != 0:
            for i, v in enumerate(args):
                if i == 0:
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif i == 1:
                    self.size = v
                elif i == 2:
                    self.x = v
                elif i == 3:
                    self.y = v
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return (
                {
                    "id": self.id,
                    "x": self.x,
                    "size": self.size,
                    "y": self.y
                    }
                )
