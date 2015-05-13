#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
Auther      : Hu Wenchao
Description : Form a data structure like defaultdict, the key is path of file,
                and return handler of the file. If there is no handler for the
                file, create one and return. If this way, we do not need to open
                and close the file again and again, also we can use try/finally
                statements to ensure all the files are closed.
'''
from collections import defaultdict

class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret

def file_write_handler(path):
    return open(path, 'a')

file_handler_dic = keydefaultdict(file_write_handler)

# write number from 1 to 10000 to files depending on its remainder.

# the direct way. We need to open and close files for 10000 times.
for i in range(10000):
    with open('log%02d' % (i % 10), 'a') as f:
        f.write('%d\n' % i)

# The way use defaultdict. Open the file when needed, and close them at last.
try:
    for i in range(10000):
        file_handler_dic['log%02d' % (i % 10)].write('%d\n' % i)
finally:
    for f in file_handler_dic.values():
        f.close()
