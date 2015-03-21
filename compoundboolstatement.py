#! /usr/bin/env python3
"""readable way of checking existence of elements in list, dict or tuple"""

l = [1, 2, 3]

if 1 and 2 and not 4 in l:
    print('check!')