#! /usr/bin/env python3
"""loop over dicts that share (some) keys"""

dctA = {'a': 1, 'b': 2, 'c': 3}
dctB = {'b': 4, 'c': 5, 'd': 6}

for ky in set(dctA) & set(dctB):
    print(ky)
