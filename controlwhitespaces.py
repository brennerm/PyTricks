#! /usr/bin/env python3
"""control the whitespaces in string"""

s = 'The Little Price'

# justify string to be at least width wide
# by adding whitespaces
width = 20
s1 = s.ljust(width)
s2 = s.rjust(width)
s3 = s.center(width)
print(s1)   # 'The Little Price    '
print(s2)   # '    The Little Price'
print(s3)   # '  The Little Price  '

# strip whitespaces in two sides of string
print(s3.lstrip())  # 'The Little Price  '
print(s3.rstrip())  # '  The Little Price'
print(s3.strip())   # 'The Little Price'
