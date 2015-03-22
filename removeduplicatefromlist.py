#! /usr/bin/env python3
"""remove duplicate items from list. Does not preserve order"""

items = [1, 2, 2, 3, 3, 3]

newitems2 = list(set(items))
print(newitems2)


