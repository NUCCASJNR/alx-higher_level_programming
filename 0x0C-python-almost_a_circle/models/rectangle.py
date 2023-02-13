#!/usr/bin/python3

"""The rectangle.py module"""

from models.base import Base


class Rectangle(Base):
    """The rectangle class that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the function
            creating an instance of the rectangle
            Args:
                width - width of the rectangle
                height - height of the rectangle
                x - 0
                y - 0
                id - None
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute."""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute."""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x attribute."""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y attribute."""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance."""

        return self.__height * self.__width

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""

        for a in range(self.__y):
            print()

        for b in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns str representation of the rectangle"""

        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the class Rectangle by adding the public method
            def update(self, *args): that assigns an argument to
            each attribute

            Args:
                id = 1st argument
                width = 2nd argument
                height = 3rd argument
                x = 4th argument
                y = 5th argument
        """

        for i, v in enumerate(args):
            if args and len(args) != 0:
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.width = v
                elif i == 2:
                    self.height = v
                elif i == 3:
                    self.x = v
                elif i == 4:
                    self.y = v

            else:
