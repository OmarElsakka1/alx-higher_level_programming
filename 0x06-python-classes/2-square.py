#!/usr/bin/python3
"""Square module"""


class Square:
    """This defines a square class"""

    def __init__(self, size=0):
        """
        Args:
            size: size of square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
