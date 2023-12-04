#!/usr/bin/python3
"""This defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """This check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If return True if obj is an instance or(inherited) instance of a_class, or False in case of failure.
    """
    if isinstance(obj, a_class):
        return True
    return False
