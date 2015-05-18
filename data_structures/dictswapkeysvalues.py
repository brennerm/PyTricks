#! /usr/bin/env python3
"""Swaps keys and values in a dict"""

_dict = {"one": 1, "two": 2}
# make sure all of dict's values are unique
assert len(_dict) == len(set(_dict.values()))
reversed_dict = {v: k for k, v in _dict.items()}