#!/usr/bin/env python3
"""nested functions"""
def addBy(val):
    def func(inc):
        return val + inc
    return func

addFive = addBy(5)
print(addFive(4))

addThree = addBy(3)
print(addThree(7))    
