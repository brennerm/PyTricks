#! /usr/bin/env python3
"""simple tuple and dictionary unpacking"""
def product(a, b):
    return a * b

def fn_iterable():
    return [2, 3]

def fn_dict():
    return {'a': 2, 'b': 3}

argument_tuple = (2, 3)
argument_dict = {'a': 2, 'b': 3}

print(product(*argument_tuple))
print(product(**argument_dict))

# unpacking works as well on function return values
print(product(*fn_iterable()))
print(product(**fn_dict()))
