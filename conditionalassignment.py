#! /usr/bin/env python3
"""Python has several ways to do conditional assignments

The first is a fairly standard ternary style;
<value if true> if <conditional> else <value if false>

The second method uses dictionary's keys to "choose" the correct value.
It's a very useful switch-case replacement.

The third method takes advantage of the fact that python's or is lazy. When
an assignment is made if the first value is falsy (None is falsy), then it will
automatically return the second value, even if that value is falsy.

"""

condition = True

b = 't' if condition else 'f'
print(b)

b = {True: 't', False: 'f', None: 'n'}.get(condition, 'default')
print(b)

b = None or False
print(b)
