#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        ma = int('-inf')
        for i in a_dictionary:
            if a_dictionary[i] > ma:
                ma = a_dictionary[i]
        return (ma)
