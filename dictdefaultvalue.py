"""
When update value in a dict based on the old value, we usually check whether
the key is in the dict. But with `dict.setdefault`, `dict.get` and
`collections.defaultdict` the code can be shorter and cleaner.

Before:
    >>> d = {}
    >>> if 'a' not in d:  # update a list
    ...     d['a'] = []
    ...
    >>> d['a'].append(1)
    >>>
    >>> if 'b' not in d:  # update an integer
    ...     d['b'] = 0
    ...
    >>> d['b'] += 1

Now:
    >>> d = {}
    >>> d.setdefault('a', []).append(1)
    >>> d['b'] = d.get('b', 0) + 1
"""

""" builtin dict """
d = {}
d.setdefault('a', []).append(1)
d['b'] = d.get('b', 0) + 1

print(d)


""" with collections.defaultdict """
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)

print(d)
