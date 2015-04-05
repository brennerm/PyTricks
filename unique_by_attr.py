#! /usr/bin/env python3
"""
    If we have some sequence of objects and want to remove items with the same attribute value
    Python creates a dict, where keys are value if attribute (bar in our case), values are object of the sequence.
    After that the dict is transformed back to list

    Note: in result we save the last from repeating elements (item2 in our case)!
"""


class Foo():
    pass


item1 = Foo()
item1.bar = 15

item2 = Foo()
item2.bar = 15

item3 = Foo()
item3.bar = 5

lst = [item1, item2, item3]

unique_lst = list({getattr(obj, 'bar'): obj for obj in lst}.values())

print(unique_lst)  # [item2, item3]
