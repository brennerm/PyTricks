#! /usr/bin/env python3
"""reversing list with special case of slice step param"""
a = [5, 4, 3, 2, 1]
print(a[::-1])

"""iterating over list contents in reverse efficiently."""
for ele in reversed(a):
    print(ele)

"""keep the initial order, but iterate over it in reverse"""
for i in range(len(a)-1, 0, -1):
    print(a[i])
