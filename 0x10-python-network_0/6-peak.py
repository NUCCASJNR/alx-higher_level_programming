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
    long = len(list_of_integers) - 1
    small = 0
    for small in range(long):
        mid = (long + small) // 2
        if list_of_integers[mid] < list_of_integers[mid+1]:
            small = mid + 1
        else:
            long = mid
    return list_of_integers[small]
