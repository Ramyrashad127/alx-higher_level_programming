#!/usr/bin/python3
def safe_print_integer(value):
    i = 0
    try:
        print("{:d}".format(value))
        i = 1
    except (TypeError, ValueError):
        i = 0
    if i:
        return True
    return False
