#!/usr/bin/python3

"""class MyList that inherits from list"""


class MyList(list):
    """initializing the class"""

    def print_sorted(self):
        """Prints sorted list"""

        print (sorted(self))
