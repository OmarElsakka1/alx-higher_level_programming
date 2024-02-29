#!/usr/bin/python3
"""This Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """finding the peak in a list of unsorted integers"""
    max_idx = None
    for element in list_of_integers:
        if max_idx is None or max_idx < element:
            max_idx = element
    return max_idx
