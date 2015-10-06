#! /usr/bin/env python3
"""Context managers are useful for automatically releasing resources once you are done with them."""

# common context manager that will close 
# a file when it has been read
with open('README.md') as f:
    contents = f.read()


# make your own context manager
import contextlib

@contextlib.contextmanager
def unlock(resource):
    resource = "unlocked"
    try:
        yield resource
    finally:
        resource = "locked"


# a resource that is locked
resource = "locked" 

# test that it is indeed locked
print(resource)

# call your 'unlock' context manager with your resource
with unlock(resource) as unlocked:
    print(unlocked) # check that it is unlocked

# ensure it was re-locked when it left the 'unlock' context
print(resource)







