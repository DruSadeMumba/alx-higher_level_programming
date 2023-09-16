#!/usr/bin/python3
"""Base class"""
import json
import csv


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
        return json.dumps(list_dictionaries) if list_dictionaries else []

    @classmethod
    def save_to_file(cls, list_objs):
        """save to json file"""
        fileJson = f"{cls.__name__}.json"
        objs = [] if not list_objs \
            else [cls.to_dictionary(o) for o in list_objs]
        with open(fileJson, "w", encoding="utf-8") as f:
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
        fileJson = f"{cls.__name__}.json"
        try:
            with open(fileJson, "r") as f:
                return [cls.create(**dic) for dic in json.load(f)]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv"""
        fileCsv = f"{cls.__name__}.csv"
        attributes = cls.sqOrder if cls.__name__ == "Square" else cls.recOrder
        with open(fileCsv, 'w', newline='') as f:
            for obj in list_objs:
                csv.writer(f).writerow([getattr(obj, attr)
                                        for attr in attributes])

    @classmethod
    def load_from_file_csv(cls):
        """load from csv"""
        fileCsv = f"{cls.__name__}.csv"
        attributes = cls.sqOrder if cls.__name__ == "Square" else cls.recOrder
        objects = []
        with open(fileCsv, 'r', newline='') as f:
            for line in csv.reader(f):
                dic = {attr: int(val) for attr, val in zip(attributes, line)}
                objects.append(cls.create(**dic))
            return objects

    def draw(list_rectangles, list_squares):
        pass
