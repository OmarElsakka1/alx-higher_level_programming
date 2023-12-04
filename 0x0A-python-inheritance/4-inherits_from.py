#!/usr/bin/python3
"""This defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """checks if object is an instance of the specified class or its parents"""
    return isinstance(obj, a_class) and type(obj) != a_class
