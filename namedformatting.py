#! /usr/bin/env python3
"""easy string formatting using dicts"""

d = {'name': 'Jeff', 'age': 24}
print("My name is %(name)s and I'm %(age)i years old." % d)

"""for .format, use this method"""

d = {'name': 'Jeff', 'age': 24}
print("My name is {name} and I'm {age} years old.".format(**d))
