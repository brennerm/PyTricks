#! /usr/bin/env python3
"""calling different functions with same arguments based on condition"""
def product(a, b):
    return a * b

def subtract(a, b):
    return a - b

b = True
print((product if b else subtract)(1, 1))
