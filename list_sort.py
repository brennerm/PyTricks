#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
Auther      : Hu Wenchao
Description : Sort a string list case insensive.
'''
import random
import string
random.seed(0)

alist = [''.join([random.choice(string.ascii_letters) for _ in range(int(5+random.random()*5))]) for _ in range(100)]
print('before sort:', alist)

sorted_alist = sorted(alist, key=lambda s: s.lower())
print('after sort:', sorted_alist)
