#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        z = ord(str[i])
        if z < 123 and z >= 97:
            str[i] = chr(z - 32)
            if i == len(str) - 1:
                print(str[i])
                break;
            print(str[i], end='')
