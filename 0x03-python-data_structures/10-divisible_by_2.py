#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list or len(my_list) == 0:
        return None
    out = []
    for num in my_list:
        if num % 2 == 0:
            out.append(True)
        else:
            out.append(False)
    return out
