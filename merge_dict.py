#! /usr/bin/env python3.5
"""merge dict's"""

d1 = {'a': 1}
d2 = {'b': 2}

#  python 3.5
print({**d1, **d2})

print(dict(d1.items() | d2.items()))

d1.update(d2)
print(d1)
