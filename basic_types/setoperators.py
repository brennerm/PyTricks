#! /usr/bin/env python3
"""Python provides usual set operator"""
a = set(['a', 'b', 'c', 'd'])
b = set(['c', 'd', 'e', 'f'])
c = set(['a', 'c'])

# Intersection
print(a & b)

# Subset
print(c < a)

# Difference
print(a - b)

# Symmetric Difference
print(a ^ b)

# Union
print(a | b)

"""using methods instead of operators which take any iterable as a second arg"""

a = {'a', 'b', 'c', 'd'}
b = {'c', 'd', 'e', 'f'}
c = {'a', 'c'}

print(a.intersection(["b"]))

print(a.difference(["foo"]))

print(a.symmetric_difference(["a", "b", "e"]))

print(a.issuperset(["b", "c"]))

print(a.issubset(["a", "b", "c", "d", "e", "f"]))

print(a.isdisjoint(["y", 'z']))

print(a.union(["foo", "bar"]))

a.intersection_update(["a", "c", "z"])
print(a)
