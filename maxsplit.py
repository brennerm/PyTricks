#! /usr/bin/env python3
"""split a string max times"""
string = "a_b_c"
print(string.split("_", 1))


"""use maxsplit with  arbitrary whitespace"""

s = "foo    bar   foobar foo"

print(s.split(None, 2))
