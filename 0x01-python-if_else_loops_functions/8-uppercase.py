#!/usr/bin/python3
def uppercase(str):
    out = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - (ord('a') - ord('A')))
        out += c
    print("{}".format(out))
