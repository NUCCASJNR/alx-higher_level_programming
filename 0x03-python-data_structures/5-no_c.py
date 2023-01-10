#!/usr/bin/python3
def no_c(my_string):
    new_copy = my_string.translate({ord(i): "" for i in 'cC'})
    return new_copy
