#! /usr/bin/env python3
"""Run common method of big sequence of objects"""
import operator


class Foo():
    def bar(self, *args, **kwargs):
        print('method bar works')


sequence = [Foo() for i in range(5)]

# in python3 map returns iterator so we must ask python to process elements by list()
# in python2 map(operator.methodcaller('bar'), sequence) works perfectly
list(map(operator.methodcaller('bar'), sequence))

# there is another way more understandable
[f.bar() for f in sequence]
