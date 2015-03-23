#! /usr/bin/env python3
""" Return the value of the named attribute of an object """
class obj():
    attr = 1

foo = "attr"
print(getattr(obj, foo))
