#! /usr/bin/env python3
"""lightweight switch statement"""
a = {
    True: 1,
    False: -1,
    None: 0
}
print(a.get(False, 0))

"""works with functions as well"""
def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b
    
b = {
    '+': add,
    '-': subtract
}

print(b['+'](1, 1))

"""

    ---- Other Way ----
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
