#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    cnt = len(argv)
    if cnt == 1:
        print("{} arguments.".format(cnt - 1))
    elif cnt > 1:
        if cnt == 2:
            print("{} argument:".format(cnt - 1))
        elif cnt > 2:
            print("{} arguments:".format(cnt - 1))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
