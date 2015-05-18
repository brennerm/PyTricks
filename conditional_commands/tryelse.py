""" You can have an 'else' clause with try/except. 
    It gets excecuted if no exception is raised.
    This allows you to put less happy-path code in the 'try' block so you can be 
    more sure of where a caught exception came from."""

try:
    1 + 1
except TypeError:
    print("Oh no! An exception was raised.")
else:
    print("Oh good, no exceptions were raised.")
