#!/usr/bin/python3
"""This module contains the class Base"""
import json
import turtle


class Base:
    """The class base"""
    __nb_object = 0

    def __init__(self, id=None):
        """The initialization function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the string representation of list dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, listobjs):
        """Save the representation of listobjs to a file"""
        filename = "{}.json".format(cls.__name__)
        with (open(filename, "w", encoding="utf-8")) as f:
            if listobjs is None or listobjs == []:
                f.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in listobjs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list represented by json_string"""
        if json_string is None or json_string == "[]":
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all the attributes set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                ret = cls(1, 1)
            else:
                ret = cls(1)
            ret.update(**dictionary)
            return (ret)

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        try:
            filename = cls.__name__ + ".json"
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with (open(filename, "w", encoding="utf-8")) as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                st = ""
                if cls.__name__ == "Rectangle":
                    for i in list_dicts:
                        st += ",".join([str(w) for w in (i["id"], i["width"],
                                        i["height"], i["x"], i["y"])])
                        st += "\n"
                else:
                    for i in list_dicts:
                        st += ",".join([str(w) for w in (i["id"], i["size"],
                                        i["x"], i["y"])])
                        st += "\n"
                f.write(st[:-1])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances"""
        try:
            filename = cls.__name__ + ".csv"
            with open(filename, "r") as f:
                a = f.read()
                if a == "[]":
                    return ([])
                li = [[int(i) for i in v.split(",")] for v in a.split()]
                return [cls(*i[1:], i[0]) for i in li]
        except FileNotFoundError:
            return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ A function that opens a window and draws all the
        Rectangles and Squares"""
        t = turtle.Turtle()
        t.screen.bgcolor("gold")
        t.hideturtle()
        t.pensize(4)
        t.color("blue")
        t.fillcolor("yellow")
        t.penup()
        for i in list_rectangles:
            t.goto(i.x, i.y)
            t.pendown()
            t.fd(i.width)
            t.right(90)
            t.fd(i.height)
            t.right(90)
            t.fd(i.width)
            t.right(90)
            t.fd(i.height)
            t.penup()
        t.color("black")
        for i in list_squares:
            t.goto(i.x, i.y)
            t.pendown()
            t.fd(i.width)
            t.right(90)
            t.fd(i.height)
            t.right(90)
            t.fd(i.width)
            t.right(90)
            t.fd(i.height)
            t.penup()
        turtle.exitonclick()
