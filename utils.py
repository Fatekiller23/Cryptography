# -*- coding: utf-8 -*-
"""
this file offers some helper function.
Normally, can be used by the most of general ciphers.
"""


def char_to_binary_string(char):
    return bin(ord(char))[2:]


def binary_string_to_char(binary_string):
    return chr(int(binary_string, 2))
