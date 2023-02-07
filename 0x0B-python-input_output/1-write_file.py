#!/usr/bin/python3

"""1-write_file.py module"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
    and returns the number of characters written
    Arguments:
                filename: file to be written into
                text: new content
    """

    with open(filename, "w+") as a:
        return a.write(text)
