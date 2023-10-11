#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
        lis = []
        for j in range(len(matrix[i])):
            lis.append(matrix[i][j]**2)
        new.append(lis)
    return (new)
