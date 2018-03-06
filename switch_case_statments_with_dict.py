#! /usr/bin/env python3

"""
	Switch/Case statments with Dictionaries 
   	Based on Dan Bader video: https://www.youtube.com/watch?v=gllUwQnYVww
"""

def traditional(operator, x , y):
	if operator == 'add':
		return x + y
	elif operator == 'sub':
		return x - y
	elif operator == 'mul':
		return x * y
	elif operator == 'div':
		return x / y


def with_dict(operator, x ,y):
	return {
		'add' : lambda: x + y,
		'sub' : lambda: x - y,
		'mul' : lambda: x * y,
		'div' : lambda: x / y,
	}.get(operator, lambda: None)()
