#!/usr/bin/python3
"""Defines a class MyList"""


class MyInt(int):
    """Initializes int operators == and !="""
 
    def __eq__(self, value):
        """Overide == operator != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Rewrites != operator with == behavior"""
        return self.real == value
