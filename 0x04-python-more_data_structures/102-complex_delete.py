#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lis_kys = list(a_dictionary.keys())
    for value_di in lis_kys:
        if value == a_dictionary.get(value_di):
            del a_dictionary[value_di]
    return (a_dictionary)
