#!/usr/bin/python3
""" Module containing class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """ Body of rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing attributes of obj"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Obtais value for rectangle width"""
        return self.__width

    @property
    def height(self):
        """Obtains value for rectangle height"""
        return self.__height

    @property
    def x(self):
        """Obtains the value x"""
        return self.__x

    @property
    def y(self):
        """Obtains value for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the valus for width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the value for height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """sets tx value"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets y value"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """Displays rectangle using # sign """
        for y in range(self.y):
            print("")
        for r in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for c in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Defines the string representation of class"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
 {self.width}/{self.height}"

    def update(self, *args, **n_args):
        """Assigns argumentt to each attribte"""
        if args and len(args) != 0:
            x = 0
            for ag in args:
                if x == 0:
                    if ag is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a = a + 1
        elif n_args and len(n_args) != 0:
            for x, y in n_args.items():
                if x == "id":
                    if y is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = y
                elif x == "width":
                    self.width = y
                elif x == "height":
                    self.height = y
                elif x == "x":
                    self.x = y
                elif x == "y":
                    self.y = y

    def to_dictionaty(self):
        """Returns dictionary representation of a rectangle"""
        o_d = {"id": self.id, "width": self.__width,
               "height": self.__height, "x": self.__x,
               "y": self.__y}
        return o_d
