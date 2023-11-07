#!/usr/bin/python3
"""module"""


class Student:
    """new"""
    def __init__(self, first_name, last_name, age):
        """new"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """new"""
        return self.__dict__
