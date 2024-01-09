#!/usr/bin/python3
""" Module defining class Student """


class Student:
    """Body of student"""
    def __init__(self, first_name, last_name, age):
        """Initianlize Public attributes"""
        self.first_name = first_name
        self.last_name - last_name
        self.age = age

    def to_json(self, attrs=None):
        """A dictionary representatio of Student in alist"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
