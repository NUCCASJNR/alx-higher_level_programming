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

    def update(self, *args, **kwargs):
        """Assigning attributes
            Args:
                    *args - list of arguments
                    id - 1st argument
                    size - 2nd argument
                    x - 3rd argument
                    y - 4th argument
        """

        if args and len(args) != 0:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.size = v
                elif i == 2:
                    self.x = v
                elif i == 3:
                    self.y = 4

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "y":
                    self.y = value
                elif key == "x":
                    self.x = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square
            Args:
                id = 1st key
                size = 2nd key
                x = 3rd key
                y = 4th key
        """

        return (
                {
                    "id": self.id,
                    "size": self.size,
                    "x": self.x,
                    "y": self.y
                    }
                )
