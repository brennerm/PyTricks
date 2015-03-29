#! /usr/bin/env python3

"""
Convert raw string integer inputs to integers
"""

str_input = input("Enter your string input\n")

print("### Input ###")
print(str_input)

int_input = [int(i) for i in str_input.split()]

print("### Output ###")
print(int_input)
