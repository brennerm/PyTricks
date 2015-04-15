#! /usr/bin/env python3
"""calling different functions with same arguments based on condition"""


def product(a, b):
    return a * b


def subtract(a, b):
    return a - b

b = True

function = product if b else subtract
result = function(1, 1)
print(result)

function = {True: product, False: subtract}[b]
result = function(1, 1)
print(result)
