#!/usr/bin/python3

"""2-append_write.py module"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    Arguments:
                filename: file to be appended into
                text: text to append
    """

    with open(filename, "a+") as a:
        return a.write(text)
