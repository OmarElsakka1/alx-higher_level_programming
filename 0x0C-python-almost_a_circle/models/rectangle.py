#!/usr/bin/python3
""" rect module """
from models.base import Base


class Rectangle(Base):
    """ rect class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val > 0:
            self.__width = val
        else:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val > 0:
            self.__height = val
        else:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """returns area"""
        return self.width * self.height

    def display(self):
        """prints rect #"""
        dispChar = '#'
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + dispChar * self.width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def __update(self, *args):
        """update vals (id, w, h, x, y)"""
        if len(args) > 0 and args[0] is not None:
            self.id = args[0]
        if len(args) > 1 and args[1] is not None:
            self.width = args[1]
        if len(args) > 2 and args[2] is not None:
            self.height = args[2]
        if len(args) > 3 and args[3] is not None:
            self.x = args[3]
        if len(args) > 4 and args[4] is not None:
            self.y = args[4]

    def update(self, *args, **kwargs):
        """update vals (id, w, h, x, y)"""
        if args:
            self.__update(*args)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return dict of rect"""
        d = dict()
        d['id'] = self.id
        d['width'] = self.width
        d['height'] = self.height
        d['x'] = self.x
        d['y'] = self.y
        return d
