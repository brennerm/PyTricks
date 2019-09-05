#!/usr/bin/env python3
"""
This program lets you create a simple command line calculator without using
the 'if..else' construct. It uses built-in 'operator' module to accomplish the
same

Created with help of an answer on stackoverflow. Don't have the exact link.
"""

import operator
ops = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow
}

print(ops['-'](50, 25))
