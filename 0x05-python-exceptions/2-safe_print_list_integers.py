#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        ele = 0
        for i in range(x):
            print("{:d}".format(my_list[i], end=""))
            ele += 1;
    except (ValueError, TypeError):
        pass
    print()
    return (ele)

