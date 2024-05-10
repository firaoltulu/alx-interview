#!/usr/bin/python3
"""
UTF-8 Validation.
"""


def validUTF8(data):
    """
    this Function list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False.
    """
    loc = 0

    for ind in data:
        if loc == 0:
            if ind >> 5 == 0b110 or ind >> 5 == 0b1110:
                loc = 1
            elif ind >> 4 == 0b1110:
                loc = 2
            elif ind >> 3 == 0b11110:
                loc = 3
            elif ind >> 7 == 0b1:
                return False
        else:
            if ind >> 6 != 0b10:
                return False
            loc -= 1
    return loc == 0
