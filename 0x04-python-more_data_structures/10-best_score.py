#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        ma = float('-inf')
        for i in a_dictionary:
            if a_dictionary[i] > ma:
                key = i
                ma = a_dictionary[i]
        return (key)
    return (None)
