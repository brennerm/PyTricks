#! /usr/bin/env python3
"""Analogue of switch statement"""
b = False
a = {
    True: 1,
    False: -1,
    None: 0
}[b]
print(a)
