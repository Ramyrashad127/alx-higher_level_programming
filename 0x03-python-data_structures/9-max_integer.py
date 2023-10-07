#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    c = my_list[0]
    for num in my_list:
        if num >= c:
            c = num
    return (c)
