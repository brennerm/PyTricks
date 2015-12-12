"""
True and False are keywords in python3, but not in Python2. In Python2
the value of True is 1, and the value of False is 0. True and False can be
regarded as vars and thus they are slow in while loop.

By the way, True and False can be changed in Python2.

Note: This leads to a performance improvement only in Python2.
"""

from timeit import timeit


def test_true():
    count = 1000
    while True:  # here is True
        if count < 0:
            break
        count -= 1


def test_1():
    count = 1000
    while 1:  # here is 1
        if count < 0:
            break
        count -= 1


# on my macbook pro 15
# test_true is about 59.3047289848 seconds
# test_1 is about 39.0966179371 seconds
print(timeit(test_true, number=1000000))
print(timeit(test_1, number=1000000))


# True and False can be changed in python2
True = 0
False = 100

print(True)
print(False)
