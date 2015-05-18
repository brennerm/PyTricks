#! /usr/bin/env python3
"""Python has two ways to do conditional assignments

The first is a fairly standard teranary style;
<value if true> if <conditional> else <value if false>

The second method takes advantage of the fact that python's or is lazy. When
an assignment is made if the first value is falsy (None is falsy), then it will
automatically return the second value, even if that value is falsy.

"""
b = True
print(True if b else False)

b = None or False
print(b)
