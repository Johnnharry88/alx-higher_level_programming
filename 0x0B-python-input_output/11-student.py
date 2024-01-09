#!/usr/bin/python3
""" Module defining class Student """


class Student:
    """Body of student"""
    def __init__(self, first_name, last_name, age):
        """Initianlize Public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A dictionary representatio of Student in alist"""
        if attrs is not None:
            xty = {k: self.__dict__[k] for k in self.__dict__.keys() & attrs}
            return xty
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Reolaces all attrributes of students"""
        for x, y in json.items():
            setattr(self, x, y)
