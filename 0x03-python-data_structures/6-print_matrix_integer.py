#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        print()
    if matrix:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end='')
                if j == len(matrix[i]) - 1:
                    print()
                else:
                    print(", ", end='')
