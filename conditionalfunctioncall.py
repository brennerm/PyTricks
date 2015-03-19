#! /usr/bin/env python3
"""calling different functions with same arguments based on condition"""
def sum(a, b):
    return a + b
    
def subtract(a, b):
    return a - b
    
b = True
print((sum if b else subtract)(1, 1))