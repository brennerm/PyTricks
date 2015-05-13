#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
Auther      : Hu Wenchao
Description :
'''
from collections import defaultdict

class keydefaultdict(defaultdict):
    '''构造一个数据结构，类似defaultdict，传入文件路径，返回对应的写文件handler。
    如果不存在则创建一个。在所有操作阶数后，关闭改字典中所有的文件。
    这样可以避免反复开关文件的开销，且可以进行容错处理，保证文件全都关闭。
    '''
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret

def file_write_handler(path):
    return open(path, 'a')

file_handler_dic = keydefaultdict(file_write_handler)

try:
    for i in range(1000):
        file_handler_dic['log%02d' % (i % 10)].write('%04d\n' % i)
finally:
    for f in file_handler_dic.values():
        f.close()
