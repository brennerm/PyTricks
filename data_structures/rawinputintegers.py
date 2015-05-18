#! /usr/bin/env python3

"""
Convert raw string integer inputs to integers
"""

str_input = "1 2 3 4 5 6"

print("### Input ###")
print(str_input)

int_input = map(int, str_input.split())

print("### Output ###")
print(list(int_input))
