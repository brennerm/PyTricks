#! /usr/bin/env python3
"""converts list to comma separated string"""

items = ['foo', 'bar', 'xyz']

print (','.join(items))

"""list of numbers to comma separated"""
numbers = [2, 3, 5, 10]

print (','.join(map(str, numbers)))

"""list of mix  data"""
data = [2, 'hello', 3, 3.4]

print (','.join(map(str, data)))


