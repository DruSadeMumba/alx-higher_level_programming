#!/usr/bin/python3
"""Base class"""
import json
import csv
from turtle import *


class Base:
    """Base class"""
    __nb_objects = 0
    sqOrder = ['id', 'size', 'x', 'y']
    recOrder = ['id', 'width', 'height', 'x', 'y']

    def __init__(self, id=None):
        """class constructor"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json str"""
        return [] if list_dictionaries is None or list_dictionaries == [] \
            else json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to json file"""
        file_json = f"{cls.__name__}.json"
        objs = [] if not list_objs \
            else [cls.to_dictionary(o) for o in list_objs]
        with open(file_json, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """json str"""
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from json"""
        file_json = f"{cls.__name__}.json"
        try:
            with open(file_json, "r") as f:
                dic = cls.from_json_string(f.read())
                return [cls.create(**dic) for i, dic in enumerate(dic)]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv"""
        file_csv = f"{cls.__name__}.csv"
        attributes = cls.sqOrder if cls.__name__ == "Square" else cls.recOrder
        with open(file_csv, 'w', newline='') as f:
            for obj in list_objs:
                csv.writer(f).writerow([getattr(obj, attr)
                                        for attr in attributes])

    @classmethod
    def load_from_file_csv(cls):
        """load from csv"""
        file_csv = f"{cls.__name__}.csv"
        attributes = cls.sqOrder if cls.__name__ == "Square" else cls.recOrder
        objects = []
        with open(file_csv, 'r', newline='') as f:
            for line in csv.reader(f):
                dic = {attr: int(val) for attr, val in zip(attributes, line)}
                objects.append(cls.create(**dic))
            return objects

    @staticmethod
    def draw_shapes(shape_list, colour):
        Turtle().screen.bgcolor("#fafad")
        Turtle().pensize(3)
        Turtle().shape("classic")

        Turtle().color(colour)
        for shap in shape_list:
            Turtle().showturtle()
            Turtle().up()
            Turtle().goto(shap.x, shap.y)
            Turtle().down()
            for _ in range(2):
                Turtle().forward(shap.width)
                Turtle().left(90)
                Turtle().forward(shap.height)
                Turtle().left(90)
            Turtle().hideturtle()
        exitonclick()

    @staticmethod
    def draw(list_rectangles, list_squares):
        Base.draw_shapes(list_rectangles, "#000000")
        Base.draw_shapes(list_squares, "#ffff00")
