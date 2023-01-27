#!/usr/bin/python3
"""a class Square that defines a square by: (based on 6-square.py)"""

class Square:
    """Initialize the square class"""

      def __init__(self, size=0, position=(0, 0)):
          """Creates a square
          Args:
            size: length of the square
            position: position of the square
          """

          self.size = size
          self.position = position

     @property

