#!/usr/bin/env python3
def no_c(my_string):
    out = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            out += char
    return out
