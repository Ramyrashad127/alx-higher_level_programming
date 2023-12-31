#!/usr/bin/python3
""" module """


class Rectangle:
    """ define """
    def __init__(self, width=0, height=0):
        """ initialize
        args:
            width: 0
            height: 0
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
