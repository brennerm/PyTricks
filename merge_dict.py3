"""merge dict's"""

d1 = {'a': 0, 'b':1}
d2 = {'b': 2, 'c':3}

print(d1 | d2)
print(d2 | d1)

print({**d1, **d2})
print({**d2, **d1})

print(dict(d1.items() | d2.items()))
print(dict(d2.items() | d1.items()))
