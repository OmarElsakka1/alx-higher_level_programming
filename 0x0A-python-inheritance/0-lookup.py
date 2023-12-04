#!/usr/bin/python3
"""This defines an object attribute lookup function."""


def lookup(obj):
    """This return a list of an object's available attributes."""
    return (dir(obj))
