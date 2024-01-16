#!/usr/bin/python3
'''Module'''


class Student:
    def __init__(self, first_name, last_name, age):
        '''init'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''return json'''
        attr_dict = self.__dict__
        if attrs is None:
            return attr_dict

        out = {}
        for key in attrs:
            val = attr_dict.get(key)
            if val is not None:
                out[key] = val

        return out

    def reload_from_json(self, json):
        """This replaces all attributes of the Student."""
        for key, val in json.items():
            setattr(self, key, val)
