#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Method for adding 2 new lines after '.?:' chars """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for ch in ".?:":
        text = (ch + "\n\n").join(
            [line.strip(" ") for line in text.split(ch)])

    print(text, end="")
