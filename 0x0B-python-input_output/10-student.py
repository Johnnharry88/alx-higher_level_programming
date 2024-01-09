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
        if attr is None:
            return self.__dict__
        else:
            dict = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dict[att] = self.__dict__[att]
            return dict_
