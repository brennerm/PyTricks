"""
Deep flattens a nested list

Examples:
    >>> list(flatten_list([1, 2, [3, 4], [5, 6, [7]]]))
    [1, 2, 3, 4, 5, 6, 7]
    >>> list(flatten_list(['apple', 'banana', ['orange', 'lemon']]))
    ['apple', 'banana', 'orange', 'lemon']
"""


# Flatten list of lists

a = [[1, 2], [3, 4]]

# Solutions:

print([x for _list in a for x in _list])

import itertools
print(list(itertools.chain(*a)))

print(list(itertools.chain.from_iterable(a)))

print(sum(a, []))

