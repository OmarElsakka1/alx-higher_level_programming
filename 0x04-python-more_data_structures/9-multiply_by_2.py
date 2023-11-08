#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for ele in a_dictionary:
        new_dict[ele] = a_dictionary[ele]
    for ele in new_dict.keys():
        new_dict[ele] = new_dict[ele] * 2
    return new_dict
