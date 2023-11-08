#!/usr/bin/python3
def square_matrix_simple(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        sub_new_matrix = []
        for j in range(len(matrix[i])):
            sub_new_matrix.append(matrix[i][j] ** 2)
        new_matrix.append(sub_new_matrix)
    return new_matrix
