#! /usr/bin/env python3

"""
	python3 has many standards data strctures inbuilt and sometimes these are very useful.
"""


#deque -> doubly ended queue.

#insertion and removal operations are faster.
# deque -> remove O(1)
# python list -> remove O(n)

from collections import deque
q = deque()

q.append('eat')
q.append('sleep')
q.append('code')

q   # output -> deque(['eat', 'sleep', 'code'])

q.popleft() # deque -> ['sleep', 'code']

