#!/usr/bin/python3
"""module"""


class Square:
    """class"""

    def __init__(self, size=0):
        """constructor
        args:
            size: len
        """
        self.__size = size

    def area(self):
        """area
        Return: area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """property for size
        Raises:
            TpeError: 1
            ValueError: 2
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size
        value: new val
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """print
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
