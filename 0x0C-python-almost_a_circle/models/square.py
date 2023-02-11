#!/usr/bin/python3

"""The square.py module that inherits from rectangle.py"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the class constructor
            Args:
                size: size of the square
                x: 0
                y: 0
                id: None
        """

        self.width = size
        self.height = size
        super().__init__(size, size,  x, y, id)

    def __str__(self):
        """"Returns a strng representation of the square instance"""

        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.height))

    @property
    def size(self):
        """Retrieves the size"""

        return self.width

    @size.setter
    def size(self, value):
        """Sets the width and the height to the same value"""

        self.width = value
        self.height = value
