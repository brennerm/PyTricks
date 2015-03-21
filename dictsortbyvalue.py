#!/usr/bin/env python3
""" Sort a dictionary by its values with the built-in sorted() function and a 'key' argument. """
 
d = {'apple': 10, 'orange': 20, 'banana': 5, 'rotten tomato': 1}
print (sorted(d.items(), key = lambda x: x[1]))
