#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_ = my_list.copy()
    list_.reverse()
    for num in list_:
        print("{:d}".format(num))
