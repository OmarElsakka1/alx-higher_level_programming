#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    for ele in set_1:
        if ele not in set_2:
            new_list.append(ele)
    for ele in set_2:
        if (ele not in set_1) and (ele not in new_list):
            new_list.append(ele)
    return set(new_list)
