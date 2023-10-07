#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        print()
    for row in matrix:
        for num in range(0, len(row)):
            print("{:d}".format(row[num]), end='')
            if num == (len(row) - 1):
                print()
            else:
                print(",", end=" ")
