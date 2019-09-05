#! /usr/bin/env python3
import sys

"""a fast way to make a shallow copy of a list"""

a = [1, 2, 3, 4, 5]
print(a[:])


"""adding an empty list yields a copy of initial list"""

a = [1, 2, 3, 4, 5]
print(a + [])  # in python3, for small lists performs faster than a[:]


"""copy list by typecasting method"""

a = [1, 2, 3, 4, 5]
print(list(a))


"""using the list.copy() method (python3 only)"""

if sys.version_info.major == 3:
    a = [1, 2, 3, 4, 5]
    print(a.copy())
else:
    # in python2 there exists the `copy` builtin module
    from copy import copy
    a = [1, 2, 3, 4, 5]
    print(copy(a))


"""copy nested lists using copy.deepcopy"""

from copy import deepcopy

l = [[1, 2], [3, 4]]

l2 = deepcopy(l)
print(l2)

