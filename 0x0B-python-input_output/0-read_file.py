#!/usr/bin/python3
'''Module'''


def read_file(filename=""):
    '''func'''
    with open(filename) as f:
        print(f.read(), end="")
