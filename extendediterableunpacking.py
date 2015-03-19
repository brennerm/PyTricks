#! /usr/bin/env python3
"""allows collecting not explicitly assigned values into 
a placeholder variable"""

a, *b, c = range(10)
print(a, b, c)