#!/usr/bin/python3
"""module"""


class Square:
    """class"""

    def __init__(self, size=0):
        """constructor
        args:
            size: len
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
    def area(self):
        """area
        Return: area
        """
        return self.__size * self.__size
