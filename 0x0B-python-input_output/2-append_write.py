#!/usr/bin/python3
"""module"""


def write_file(filename="", text=""):
    """ write"""
    with open(filename, "a", encoding="UTF-8") as fi:
        return fi.write(text)
