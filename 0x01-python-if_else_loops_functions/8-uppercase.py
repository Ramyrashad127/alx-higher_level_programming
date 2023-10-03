#!/usr/bin/python3
def uppercase(str):
    for i in str:
        asc = ord(str[i])
        if asc >= 97 and acs <=122:
            char = chr(asc - 32)
        else:
            char = chr(asc)
        print("{}".format(char), end='')
    print()
