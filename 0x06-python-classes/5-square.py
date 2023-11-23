#!/usr/bin/python3
"""Square module"""


class Square:
    """This defines a square class """

    def __init__(self, size=0):
        """
        Args:
            size: size of square
        """
        self.size = size

    def area(self):
        """Returns area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        for i in range(self.size):
            for j in range(self.size):
                print('#', end='\n' if j is self.size - 1 and i != j else "")
        print()
