#! /usr/bin/env python3
"""
    If we have some sequence of objects and want to remove items with the same attribute value
    Python creates a dict, where keys are value if attribute (bar in our case), values are object of the sequence.
    After that the dict is transformed back to list
    Note: in result we save the last from repeating elements (item2 in our case)!
"""


class Foo(object):
    def __init__(self, value):
        self.bar = value

    def __eq__(self, other):
        return self.bar == getattr(other, 'bar')
    
    def __hash__(self):
        return int(self.bar)
    
    def __repr__(self):
        return '{}'.format(self.bar)

item1 = Foo(15)
item2 = Foo(15)
item3 = Foo(5)

lst = [item1, item2, item3]


print(set(lst))

# original
unique_lst = list({getattr(obj, 'bar'): obj for obj in lst}.values())
print(unique_lst)  # [item2, item3]
