#!/usr/bin/python3
'''Module'''


def append_write(filename="", text=""):
    '''func'''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
