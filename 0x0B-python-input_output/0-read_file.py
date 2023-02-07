#!/usr/bin/python3

"""0-read_file.py module"""


def read_file(filename=""):
    """a function that reads a text file (UTF8)
    and prints it to stdout

    Args:
        flinename: this is the file to be read
    """

    with open(filename, encoding="utf-8") as a:
        read_data = a.read()
        print(read_data, end="")
