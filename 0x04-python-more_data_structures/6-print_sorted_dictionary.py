#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ele in sorted(a_dictionary.keys()):
        print("{}: {}".format(ele, a_dictionary[ele]))
