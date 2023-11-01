#!/usr/bin/python3
""" module """


def add_integer(a, b=98):
    """add two number
        args:
            a: first
            b: second
        Return: a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    res = int(a) + int(b)
    return res


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
