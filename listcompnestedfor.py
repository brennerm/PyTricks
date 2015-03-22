#! /usr/bin/env python3
"""flattening nested lists of depth 2 within a single list comprehension with
multiple for loops"""

l = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8],
    [9]
    ]

print([
    j
    for i in l
    for j in i
    ])
