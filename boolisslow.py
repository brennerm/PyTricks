"""
True and False are keywords in python3, but not in Python2. In Python2
the value of True is 1, and the value of False is 0. True and False can be
regarded as vars and thus they are slow in while loop.

By the way, True and False can be changed in Python2.

Note: This leads to a performance improvement only in Python2.
"""
import sys
from timeit import timeit


def test_true():
    count = 100
    while True:  # here is True
        if count < 0:
            break
        count -= 1


def test_1():
    count = 100
    while 1:  # here is 1
        if count < 0:
            break
        count -= 1


# test_true is about 5.01579904556 seconds
# test_1 is about 3.70646500587 seconds
print(timeit(test_true, number=1000000))
print(timeit(test_1, number=1000000))
