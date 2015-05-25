#! /usr/bin/env python3
'''
A simple way to convert arbitrary Python code into a function
'''

import math # using sin, cos and sqrt for example

''' Takes a code string and returns a ready-to-use function '''
def compile_(s):
	code = """def f(x):\n  return {}""".format(s) # wrap the string as a function f(x)
	scope = {"sin": math.sin, "cos": math.cos, "sqrt": math.sqrt} # define the scope for the code to use
	exec(code, scope) # execute code inside the given scope
	# f(x) gets defined inside %vis%
	return scope["f"] # now we only have to extract it and return

f = compile_("x**2 + 2*sin(x)")
print(f(10))