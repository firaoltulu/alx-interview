#!/usr/bin/python3
"""Firaol Tulu Task 1 - A module for working with lockboxes.
"""


def canUnlockAll(boxes):
    """This Function Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    """
    l_n = len(boxes)
    par_two = set([0])
    par_three = set(boxes[0]).difference(set([0]))
    while len(par_three) > 0:
        boxIdx = par_three.pop()
        if not boxIdx or boxIdx >= l_n or boxIdx < 0:
            continue
        if boxIdx not in par_two:
            par_three = par_three.union(boxes[boxIdx])
            par_two.add(boxIdx)
    return l_n == len(par_two)
