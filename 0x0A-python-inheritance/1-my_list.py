#!/usr/bin/python3
"""
This defines MyList that inherits from list
"""


class MyList(list):
    """
        This class is inherited from list.
        Attributes:
        Methods:
            print_sorted - prints the list in ascending order
    """
    def print_sorted(self):
        """
           This prints a list in ascending order.
        """
        print(sorted(self))
