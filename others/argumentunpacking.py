#! /usr/bin/env python3
"""simple tuple and dictionary unpacking"""
def product(a, b):
    return a * b

argument_tuple = (1, 1)
argument_dict = {'a': 1, 'b': 1}

print(product(*argument_tuple))
print(product(**argument_dict))
