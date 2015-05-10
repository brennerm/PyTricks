"""
Find Index of Min/Max Element.
"""

lst = [40, 10, 20, 30]


def minIndex(lst):
    return min(range(len(lst)), key=lst.__getitem__)  # use xrange if < 2.7


def maxIndex(lst):
    return max(range(len(lst)), key=lst.__getitem__)  # use xrange if < 2.7

print(minIndex(lst))
print(maxIndex(lst))
