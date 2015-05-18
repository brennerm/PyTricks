#! /usr/bin/env python3
"""a fast way to make a shallow copy of a list"""

a = [1, 2, 3, 4, 5]
print(a[:])

"""using the list.copy() method (python3 only)"""

a = [1, 2, 3, 4, 5]

print(a.copy())


"""copy nested lists using copy.deepcopy"""

from copy import deepcopy

l = [[1, 2], [3, 4]]

l2 = deepcopy(l)
print(l2)

