#!/usr/bin/python3
def uppercase(str):
    for i in str:
        asc = ord(i)
        if asc >= 97 and asc <= 122:
            char = chr(asc - 32)
        else:
            char = chr(asc)
        print("{}".format(char), end='')
    print()
