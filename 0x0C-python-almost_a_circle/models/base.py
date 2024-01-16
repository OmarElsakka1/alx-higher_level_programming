#!/usr/bin/python3
""" base class """
import json
import csv


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """from dict to json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """from json to dict"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string to a file"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]

        with open("{}.json".format(cls.__name__), 'w') as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the CSV string to file"""
        from models.rectangle import Rectangle
        from models.square import Square

        if list_objs is not None:
            if cls is Rectangle:
                list_objs = \
                    [[o.id, o.width, o.height, o.x, o.y] for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y] for o in list_objs]
        with open("{}.csv".format(cls.__name__), 'w', newline="") as f:
            csvWritter = csv.writer(f)
            csvWritter.writerows(list_objs)

    @classmethod
    def create(cls, **dictionary):
        """from dict to obj"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            obj = Rectangle(1, 1)
        elif cls is Square:
            obj = Square(1)
        else:
            obj = None

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        try:
            with open("{}.json".format(cls.__name__), 'r') as f:
                content = cls.from_json_string(f.read())
                output = []
                for itm in content:
                    output.append(cls.create(**itm))
                return output
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """loads from csv"""
        try:
            with open("{}.csv".format(cls.__name__), 'r', newline="") as f:
                csvReader = csv.reader(f)
                output = []
                for row in csvReader:
                    row = [int(c) for c in row]
                    if len(row) == 5:
                        d = {"id": row[0], "width": row[1],
                             "height": row[2], "x": row[3], "y": row[4]}
                    else:
                        d = {"id": row[0], "size": row[1],
                             "x": row[2], "y": row[3]}
                    output.append(cls.create(**d))
                return output
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw using turtle"""
        import turtle
        import time
        from random import randrange

        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color(randrange(255), randrange(255), randrange(255))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            time.sleep(0.1)
            t.forward(i.height)
            t.left(90)
            time.sleep(0.1)
            t.forward(i.width)
            t.left(90)
            time.sleep(0.1)
            t.forward(i.height)
            t.left(90)
            time.sleep(0.1)
            t.end_fill()
            time.sleep(0.1)
