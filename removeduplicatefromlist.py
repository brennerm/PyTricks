#! /usr/bin/env python3
"""remove duplicate items from list. note: does not preserve the original list order"""

items = [1, 2, 2, 3, 3, 3]

newitems2 = list(set(items))
print(newitems2)


