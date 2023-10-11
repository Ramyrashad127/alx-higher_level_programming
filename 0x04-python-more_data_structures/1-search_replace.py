#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) != 0:
        li = []
        for i in range(len(my_list)):
            if my_list[i] == search:
                li.append(replace)
                continue
            li.append(my_list[i])
        return (li)
