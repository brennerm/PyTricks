#! /usr/bin/env python3
"""
Deep flattens a nested list

Examples:
    >>> list(flatten_list([1, 2, [3, 4], [5, 6, [7]]]))
    [1, 2, 3, 4, 5, 6, 7]
    >>> list(flatten_list(['apple', 'banana', ['orange', 'lemon']]))
    ['apple', 'banana', 'orange', 'lemon']
"""

def flatten_list(L):
    for item in L:
        if isinstance(item, list):
            yield from flatten_list(item)
        else:
            yield item

# In Python 2
from compiler.ast import flatten
flatten(L)
