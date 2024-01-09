#!/usr/bin/python3
"""Module that defines Class Student"""


class Student:
    """Body of Class"""

    def __init__(self, first_name, last_name, age):
        """Initialize class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dict representation of student instance"""
        return self.__dict__
