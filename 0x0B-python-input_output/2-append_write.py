#!/usr/bin/python3
"""module"""


def append_write(filename="", text=""):
    """ a"""
    with open(filename, "a", encoding="UTF-8") as fi:
        return fi.write(text)
