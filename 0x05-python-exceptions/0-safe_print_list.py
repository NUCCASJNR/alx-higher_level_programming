#!/usr/bin/python3

"""my_list can contain any type (integer, string, etc.)
All elements must be printed on the same line followed by a new line.
x represents the number of elements to print
x can be bigger than the length of my_list
Returns the real number of elements printed
You have to use try: / except:
You are not allowed to import any module
You are not allowed to use len()
"""
def safe_print_list(my_list=[], x=0):
    a = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            a += 1
        except IndexError:
            break
    print("")
    return (a)
    
