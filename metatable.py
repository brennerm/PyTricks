"""
metatable with where the function receives the dictionary and key.
"""
from collections import defaultdict


class metatable(defaultdict):

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(self, key)
            return ret


def fib(d, n):
    if n == 0 or n == 1:
        return n
    return d[n - 1] + d[n - 2]

d = metatable(fib)
print(d[1])
print(d[3])
print(d[10])
print(d)
