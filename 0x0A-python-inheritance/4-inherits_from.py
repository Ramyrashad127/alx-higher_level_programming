#!/usr/bin/python3
""" module """


def inherits_from(obj, a_class):
    """ new """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
