#!/usr/bin/python3
def common_elements(set_1, set_2):
    a = []
    for ele in set_1:
        for ans in set_2:
            if ele == ans:
                a.append(ele)
                break
    return (a)
