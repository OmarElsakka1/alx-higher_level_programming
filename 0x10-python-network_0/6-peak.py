#!/usr/bin/python3
"""This Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """finding the peak in a list of unsorted integers"""
    if (not list_of_integers):
        return None

    left_idx = 0
    right_idx = len(list_of_integers) - 1

    while left_idx < right_idx:
        mid_idx = left_idx + (right_idx - left_idx) // 2

        if (mid_idx == 0
            or list_of_integers[mid_idx - 1] <= list_of_integers[mid_idx]) and \
           (mid_idx == len(list_of_integers) - 1
                or list_of_integers[mid_idx + 1] <= list_of_integers[mid_idx]):
            return list_of_integers[mid_idx]

        if mid_idx > 0 and list_of_integers[mid_idx - 1] > list_of_integers[mid_idx]:
            right_idx = mid_idx
        else:
            left_idx = mid_idx + 1

    return list_of_integers[left_idx]
