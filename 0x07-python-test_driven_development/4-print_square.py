#!/usr/bin/python3
"""Module for print_square method."""


def print_square(size):
    """Method for printing a square with # (Hashes)"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")
