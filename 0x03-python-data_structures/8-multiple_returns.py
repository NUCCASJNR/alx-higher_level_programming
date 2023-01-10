#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    my_tuple = ()
    if len(sentence) == 0:
        my_tuple = 0
        return None
    else:
        my_tuple = lenght, sentence[0]
    return my_tuple
