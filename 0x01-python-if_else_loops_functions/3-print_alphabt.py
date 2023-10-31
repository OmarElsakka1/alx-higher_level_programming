#!/usr/bin/python3
for i in range(26):
    char = chr(ord('a') + i)
    if char == 'q' or char == 'e':
        continue
    print("{}".format(char), end="")
