#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import * 

    a = dir()
    for i in range(0, len(array)):
        if array[i][0:2] != "__":
            print("{}".format(array[i]))