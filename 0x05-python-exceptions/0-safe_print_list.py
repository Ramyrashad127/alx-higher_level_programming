#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        ele = 0
        for i in range(x):
            print(my_list[i], end="")
            ele = ele + 1
    except:
        pass
    finally:
        print()
        return (ele)
