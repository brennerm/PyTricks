#! /usr/bin/env python3
"""lightweight switch statement"""
a = {
    True: 1,
    False: -1,
    None: 0
}
print(a.get(False, 0))

"""works with functions as well"""
def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b
    
b = {
    '+': add,
    '-': subtract
}

print(b['+'](1, 1))
