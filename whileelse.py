""" You can have an else clause with a while. Works like for-else.
    When break is encountered, it exits the loop without executing else. """

i = 5

while i > 1:
    print("Whil-ing away!")
    i -= 1
    if i == 3:
        break
else:
    print("Finished up!")
