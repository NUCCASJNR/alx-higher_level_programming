#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = list(my_list)
    for i in range(len(n)):
        if n[i] == search:
            n[i] = replace
    return n
