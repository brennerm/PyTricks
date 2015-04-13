#!/usr/bin/env python3
"""
	Set initial value
"""

def setDefaultOld(initial=None):
	if not initial:
		initial = 30
	return initial

def setDefaultNew(initial=None):
	initial = initial or 60
	return initial

if __name__ == "__main__":
	print(setDefaultOld())
	print(setDefaultOld(15))
	print(setDefaultNew())
	print(setDefaultNew(123))
