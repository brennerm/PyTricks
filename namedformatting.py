#! /usr/bin/env python3
"""easy string formatting using dicts"""

d = {'name': 'Jeff', 'age': 24}
print("My name is %(name)s and I'm %(age)i years old." % d)

"""for .format, use this method"""

d = {'name': 'Jeff', 'age': 24}
print("My name is {name} and I'm {age} years old.".format(**d))

"""alternate .format method"""
print("My name is {} and I'm {} years old.".format('Jeff','24'))

"""dict string formatting"""
c = {'email': 'jeff@usr.com', 'phone': '919-123-4567'}
print('My name is {0[name]}, my email is {1[email]} and my phone number is {1[phone]}'.format(d, c))

"""object string formatting"""
class Person:
  pass
me = Person()
me.name = 'Jeff'
me.email = 'jeff@usr.com'
me.phone = '919-123-4567'
print('My name is {me.name}, my email is {me.email} and my phone number is {me.phone}'.format(me=me))