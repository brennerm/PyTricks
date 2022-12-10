"""merge dict's"""

d1 = {'a': 1}
d2 = {'b': 2}
d3 = {'a': 0, 'b':1}
d4 = {'b': 2, 'c':3}

print(d1 | d2)
print(d3 | d4)
print(d4 | d3)

print({**d1, **d2})
print({**d3, **d4})
print({**d4, **d3})

print(dict(d1.items() | d2.items()))
print(dict(d3.items() | d4.items()))
print(dict(d4.items() | d3.items()))
