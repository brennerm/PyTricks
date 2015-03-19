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