#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = []
    c = 0
    for i in set_1:
        c = 0
        for j in set_2:
            if i == j:
                c = 1
        if c == 0:
            a .append(i)
    for i in set_2:
        c = 0
        for j in set_1:
            if i == j:
                c = 1
        if c == 0:
            a .append(i)
    return (a)
