#! /usr/bin/env python3

"""reversing string with special case of slice step param"""

a = 'abcdefghijklmnopqrstuvwxyz'
print(a[::-1])


"""iterating over string contents in reverse efficiently."""

for char in reversed(a):
    print(char)

"""reversing an integer through type conversion and slicing."""

num = 123456789
print(int(str(num)[::-1]))
