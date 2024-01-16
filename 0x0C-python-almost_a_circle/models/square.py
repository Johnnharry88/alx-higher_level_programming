#!/usr/bin/python3
"""Modules contains Class Squarw"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Body of a square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """sets the value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets the square value"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """Defines sring represntation of class"""
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.size}"

    def update(self, *args, **n_args):
        """Sets Arguments of an instance"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for x, y in n_args.items():
                if x == "id":
                    if type(y) != int and y is not None:
                        raise TypeError("ide must be an inteer")
                    self.id = y
                if x == "size":
                    self.size = y
                if x == "x":
                    self.x = y
                if x == "y":
                    self.y = y

    def to_dictionary(self):
        """Returns dictionary representation of Square"""
        obj_dict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return obj_dict
