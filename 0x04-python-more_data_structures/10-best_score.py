#!/usr/bin/python3
def best_score(a_dictionary):
    key = None
    ma = int('-inf')
    for i in a_dictionary:
        if a_dictionary[i] > ma:
            key = i
    return (key)
