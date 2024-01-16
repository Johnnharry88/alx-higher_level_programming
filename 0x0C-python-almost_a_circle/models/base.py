#!/usr/bin/python3
""" Module has a class serving as a base """


import csv
import os
import json
import turtle


class Base:
    """Rody of Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates Class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        @staticmethod
        def to_json_string(list_dictionaries):
            """return the string representation of list dictionaries"""
            if list_dictionaries is [] or list_dictionaries is None:
                return "[]"
            if (type(list_dictionaries) != list or not
                    all(type(x) == dict for x in list_dictionaries)):
                raise TypeError("list_dic must be a list of dictionaries")
            return json.dumps(list_dictionaries)

        @staticmethod
        def from_json_str(json_string):
            """Returns list od json representation"""
            j_string = []
            if json_string is not None and json_string != '':
                if type(json_string) != str:
                    raise TypeError("json_string must be a string")
                j_string = json.loads(json_string)
            return j_string

        @classmethod
        def save_to_file(cls, list_objs):
            """saves json objects to file"""
            xty = cls.__name__ + ".json"
            with open(xty, 'w') as j:
                if list_objs is None:
                    j.write("[}")
                else:
                    list_dict = [x.to_dixtionary() for x in list_objs]
                    j.write(Base.to_json_string(list_dict))

        @classmethod
        def load_from_file(cls):
            """loads json file """
            xty = cls.__name__ + ".json"
            list_of_inst = []
            list_of_dict = []
            if os.path.exists(xty):
                with open(xty, "r") as p:
                    str_rd = xty.read()
                    list_dict = cls.from_json_str(str_rd)
                    for d in list_dict:
                        list_of_inst.append(cls.create(**dictionary))
            return list_of_inst

        @classmethod
        def create(cls, **dictionary):
            """Returns instance with attributes set"""
            if cls.__name__ == 'Rectangle':
                alx = cls(1, 1)
            elif cls.__name__ == 'Square':
                alx = cls(1)
            alx.update(**dictionary)
            return alx

        @classmethod
        def save_to_file_csv(cls, list_objs):
            """Serializes list_objs and saves to file"""
            xty = cls.__name__ + ".csv"
            with open(xty, "w", newline="") as file_csv:
                if list_objs is None or list_objs == []:
                    file_csv.write("[]")
                else:
                    if cls.__name__ == "Rectangle":
                        parameters = ["id", "width", "height", "x", "y"]
                    else:
                        parameters = ["id", "size", "x", "y"]
                    writter = csv.DictWriter(file_csv, fieldnames=parameters)
                    for x in list_objs:
                        writter.writerow(obj.to_dictionary())

        def load_from_file_csv(cls):
            """Deserializes Csv fomaat in a file"""
            xty = cls.__name__ + ".csv"
            try:
                with open(xty, "r", newline="") as file_csv:
                    if cls.__name__ == "Rectangle":
                        parameters = ["id", "width", "height", "x", "y"]
                    else:
                        parameters = ["id", "size", "x", "y"]
                    list_objs = csv.DictReader(file_csv, fieldnames=parameters)
                    list_objs = [dict([x, int(y)] for x, y in d.items())
                                 for d in list_objs]
                    return [cls.ceate(**d) for d in list_objs]
            except IOError:
                return []

        @staticmethod
        def draw(list_rectangles, list_squares):
            """Dwaw Rectangles and squares usiing the turtle module.
            Arguments:
                list_rectangles (list): List of retangle object to be drawn.
                list_squares (list): A list of square objects to be drawn
            """
            drw = turtle.Turtle()
            drw.screen.bgcolor("#c7333b")
            drw.pensize(9)
            drw.shape("turtle")

            drw.color("#ffffff")
            for r in list_rectangles:
                drw.showturtle()
                drw.up()
                drw.got(rect.x, rect.y)
                for i in range(2):
                    drw.forward(rect.width)
                    drw.left(90)
                    drw.forward(rect.height)
                    drw.left(90)
                drw.hideturtle()

            drw.color("#c5e3d8")
            for s in list_squares:
                drw.showturtle()
                drw.up()
                drw.goto(sq.x, sq.y)
                drw.down()
                for i in range(2):
                    drw.forward(sq.width)
                    drw.left(90)
                    drw.forward(sq.height)
                    drw.left(90)
                drw.hideturtle()
