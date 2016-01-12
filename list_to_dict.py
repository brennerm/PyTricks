#! /usr/bin/env python3
"""Convert list into dictionary"""

items = ['a', 1, 'b', 2]

res = dict(zip(items[0::2], items[1::2]))
print(res)
