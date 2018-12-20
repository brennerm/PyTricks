#! /usr/bin/env python3
"""else gets called when for loop does not reach break statement"""
a = [1, 2, 3, 4, 5]
for el in a:
    if el == 0:
        break
else:
    print('did not break out of for loop')

