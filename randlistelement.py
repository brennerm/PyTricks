#! /usr/bin/env python3

"""
Get random element from list
"""
from random import randrange

my_list = range(1,10)
my_alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(my_list[randrange(len(my_list))])

print(my_alpha_list[randrange(len(my_alpha_list))])

