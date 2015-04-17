a = [[1,2], [3,4]]

# Solutions:

[x for _list in a for x in _list]

import itertools
list(itertools.chain(*a))

list(itertools.chain.from_iterable(a))

sum(a, [])
