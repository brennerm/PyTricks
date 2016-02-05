#!/usr/bin/env python

"""Determining the maximum of a list of numerical values by using reduce """

f = lambda a,b: a if (a > b) else b
print(reduce(f, [47,11,42,102,13]))
# output: 102

# calculating the sum of numbers from 1 to 100
print(reduce(lambda x, y: x+y, range(1,101)))
# output: 5050
