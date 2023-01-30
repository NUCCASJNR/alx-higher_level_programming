#!/usr/bin/python3
""" a function that prints a text with 2 new lines after
    each of these characters: ., ? and
        Args:
            .: first Args
            ,: Second Args
            ?: Third Args
        Raise: TypeError text must be a string
"""


def text_indentation(text):
    if (".") in text:
        print("\n")
        print(end="")
    elif ("?") in text:
        print("\n")
        print(text, end="")
    elif (":") in text:
        print("\n")
        print(text, end="")
    elif type(text) is not str:
        raise TypeError("text must be a string")
