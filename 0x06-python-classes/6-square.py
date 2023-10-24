#!/usr/bin/python3
"""module"""


class Square:
    """class"""

    def __init__(self, size=0, position=(0, 0)):
        """constructor
        args:
            size: len
        """
        self.__size = size
        self.__position = position

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
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """method
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set value
        """
        if ((isinstance(value, tuple)) and (len(value) == 2)):
                if value[0] > 0 and value[1] > 0:
                    self.__position = value
                else:
                    raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
