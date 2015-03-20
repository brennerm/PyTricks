#! /usr/bin/env python3
"""Reverses keys and values in a dict"""

_dict = {"one": 1, "two": 2}
# make sure dict is reversible
assert len(set(_dict.keys())) == len(set(_dict.values()))
reversed_dict = {v: k for k, v in _dict.items()}