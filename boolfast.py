"""Getting the truthyness via bool(obj) is slow because it is a global and
therefore involves multiple namespace lookups. You can use the keyword `not`
to avoid the overheard i.e. `not not obj`.
"""

import timeit

slow_setup = """
class C:
    def __init__(self):
        self.some_val = 5
    def __bool__(self):
        return bool(self.some_val)
a = C()
"""

fast_setup = """
class C:
    def __init__(self):
        self.some_val = 5
    def __bool__(self):
        return not not self.some_val
a = C()
"""

# on my machine:

# 0.433618037256565
print(timeit.timeit('a.__bool__()', slow_setup))

# 0.2220980115553175
print(timeit.timeit('a.__bool__()', fast_setup))

# 0.40519480762077364
print(timeit.timeit('if a:pass', slow_setup))

# 0.24311949953334988
print(timeit.timeit('if a:pass', fast_setup))
