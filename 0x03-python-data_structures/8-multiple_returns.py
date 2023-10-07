#!/usr/bin/python3
def multiple_returns(sentence):
    if not(sentence):
        c = None
    else:
        c = sentence[0]
    return ((len(sentence), c))
