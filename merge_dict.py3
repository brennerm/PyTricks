"""merge dict's"""

d1 = {'a': 1}
d2 = {'b': 2}

print({**d1, **d2})

print(dict(d1.items() | d2.items()))