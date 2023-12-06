#!/usr/bin/python3
'''Module'''


class Student:
    def __init__(self, first_name, last_name, age):
        '''init'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''return json'''
        return self.__dict__
