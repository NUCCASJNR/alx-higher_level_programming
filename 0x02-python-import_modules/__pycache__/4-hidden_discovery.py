#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import * 

    a = 0
    for x in sys.argv[1::]:
        a += int(x)
        print