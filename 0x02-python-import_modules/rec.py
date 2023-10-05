#!/usr/bin/python3
def pri(asc):
    if asc == 64:
        return
    pri(asc - 1)
    print(chr(asc), end='')
