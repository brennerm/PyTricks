#! /usr/bin/env python3
"""Analogue of switch statement"""
a = {
    True: 1,
    False: -1,
    None: 0
}
print(a.get(False, 0))
