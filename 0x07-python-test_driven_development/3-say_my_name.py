#!/usr/bin/python3
"""module"""


def say_my_name(first_name, last_name=""):
    """say my name
    first_name: 1
    last_name: 2
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
