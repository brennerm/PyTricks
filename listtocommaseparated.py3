data = [2, 'hello', 3, 3.4]

"""print without creating the whole string"""
print(*data, sep=',')

"""the print function and the StringIO object"""
from io import StringIO

out = StringIO()
print(*data, sep=',', end='', file=out)
print(out.getvalue())
