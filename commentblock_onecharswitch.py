#! /usr/bin/env python3
""" 
comment blocks can be turn on and off 
in one character switch when preceded by #"""

#'''
print('see me ?')
#'''

'''
print('see me too ?')
#'''

print('there is more')

""" 
This applies to turn either one block as comments
OR the next one.

In the following example, removing the first #
will comment block 1 and decomment block 2
"""

#'''
print('block 1')
'''
print('or block 2 ?')
#'''

print('nice!')
