#!/usr/bin/python3
""" sq module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ sq class """

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def __update(self, *args):
        """update vals (id, size, x, y)"""
        if len(args) > 0 and args[0] is not None:
            self.id = args[0]
        if len(args) > 1 and args[1] is not None:
            self.size = args[1]
        if len(args) > 2 and args[2] is not None:
            self.x = args[2]
        if len(args) > 3 and args[3] is not None:
            self.y = args[3]

    def update(self, *args, **kwargs):
        """Updates square"""
        if args:
            self.__update(*args)
        elif kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """return sq of rect"""
        d = dict()
        d['id'] = self.id
        d['size'] = self.size
        d['x'] = self.x
        d['y'] = self.y
        return d
