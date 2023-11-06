#!/usr/bin/python3
""" module """


class BaseGeometry:
    """ new """

    def area(self):
        """new"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ new """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ inhir """

    def __init__(self, width, height):
        """ new """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
