#!/usr/bin/python3
"""THis Question 2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """This Method Rotates an m by n 2D matrix in place."""
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return

    three = len(matrix)
    cols = len(matrix[0])

    if not all(map(lambda x: len(x) == cols, matrix)):
        return

    one, two = 0, three - 1
    for i in range(cols * three):
        if i % three == 0:
            matrix.append([])
        if two == -1:
            two = three - 1
            one += 1
        matrix[-1].append(matrix[two][one])
        if one == cols - 1 and two >= -1:
            matrix.pop(two)
        two -= 1
