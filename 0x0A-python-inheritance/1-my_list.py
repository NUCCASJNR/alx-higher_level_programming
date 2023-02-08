#!/usr/bin/python3

"""Class mylist that inherits from list"""


class MyList(list):
    """Initializing the class"""

    def print_sorted(self):
        """Prints the soretd list"""

        print(sorted(self))
