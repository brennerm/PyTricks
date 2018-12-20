#! /usr/bin/env python3
"""remove duplicate items from list. note: does not preserve the original list order"""

items = [2, 2, 3, 3, 1]

newitems2 = list(set(items))
print(newitems2)

"""remove dups and keep order"""

from collections import OrderedDict

items = ["foo", "bar", "bar", "foo"]

print(list(OrderedDict.fromkeys(items).keys()))
