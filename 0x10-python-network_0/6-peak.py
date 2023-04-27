#!/usr/bin/python3
"""
Prints peak value
"""


def find_peak(list_of_integers):
    """
    Returns peak
    """
    if len(list_of_integers) == 0:
        return None
    return (max(list_of_integers))
