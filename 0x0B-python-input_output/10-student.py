#!/usr/bin/python3
"""module"""


class Student:
    """new"""
    def __init__(self, first_name, last_name, age):
        """new"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """new"""
        try:
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        new = dict()
        for i, j in self.__dict__.items():
            if i in attrs:
                new[i] = j
        return new

