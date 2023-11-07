#!/usr/bin/python3
"""module"""


def read_file(filename=""):
    """ open file """
    with open(filename, "r", encoding= "UTF-8") as fi:
        print(fi.read(), end="")
