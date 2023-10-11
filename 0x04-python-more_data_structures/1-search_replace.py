#!/usr/bin/python3
def search_replace(my_list, search, replace):
    li = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            li.append(replace)
        li.append( my_list[i])
    return (li)

