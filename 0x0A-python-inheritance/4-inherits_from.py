#!/usr/bin/python3
"""module"""


def inherits_from(obj, a_class):
    """This checks if object is an instance of the specified class or its parents"""
    return isinstance(obj, a_class) and type(obj) != a_class
