#!/usr/bin/python3
"""mylist module"""


class MyInt(int):
    """This is mylist class"""
    def __eq__(self, __value: object) -> bool:
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        return super().__eq__(__value)
