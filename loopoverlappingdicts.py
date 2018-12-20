#! /usr/bin/env python3
"""loop over dicts that share (some) keys in Python2"""

dctA = {'a': 1, 'b': 2, 'c': 3}
dctB = {'b': 4, 'c': 3, 'd': 6}

for ky in set(dctA) & set(dctB):
    print(ky)
