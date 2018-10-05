#! /usr/bin/env python3
# Type of variable: Number
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)
# Type of variable: List
myList = [1, 2, 3, 4, 5]
print("Initial Array :", myList)
myList[0], myList[1] = myList[1], myList[0]
print("Swapped Array :", myList)
