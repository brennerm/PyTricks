#! /usr/bin/env python3
"""remove duplicate items from list"""

items = [1, 2, 2, 3, 3, 3]

newitems2 = list(set(items))
print(newitems2)

"""remove dups and keep order"""

from collections import OrderedDict

items = ["foo", "bar", "bar", "foo"]

print(list(OrderedDict.fromkeys(items).keys()))

