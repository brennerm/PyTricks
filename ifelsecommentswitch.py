#! /usr/bin/env python3
""" 
comment blocks can be turn on and off 
in one character switch when preceded by #"""

#''' #< toggling off this # turns the block as a comment (it wasn't, line was mute)
print("you saw me!")
#''' 

print("catched!")

"""
second example is the equivalent 
of C prepropressors #ifdef 0  / #ifdef 1 comment styles:   
"""

#''' < toggling this # will comment the next block,
print("you saw me now you don't see me")
'''# which will stop here, where it was previously beginning, hence turning it in the ending block tag
print("you didn't see me, now you do !")
#''' # and so, it uncomments the one below

print('continue...')
