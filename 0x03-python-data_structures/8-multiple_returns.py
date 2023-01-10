#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    if len(sentence) == 0:
        return None
    else:
        my_tuple = len(sentence), sentence[0]
        return my_tuple
