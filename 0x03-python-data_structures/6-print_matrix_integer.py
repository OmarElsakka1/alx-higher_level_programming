#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if (len(row) == 0):
            print()
        for idx, num in enumerate(row):
            print("{:d}".format(num), end="\n" if idx == len(row) - 1 else " ")
