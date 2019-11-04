"""
keydefaultdict with where the function receives the key.
"""
from collections import defaultdict


class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret


def pow2(n):
    return 1 << n 

d = keydefaultdict(pow2)
print(d[1])
print(d[3])
print(d[10])
print(d)
