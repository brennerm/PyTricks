"""allows collecting not explicitly assigned values into 
a placeholder variable"""

a, *b, c = range(10)
print(a, b, c)

"""advanced example"""

[(c, *d, [*e]), f, *g] = [[1, 2, 3, 4, [5, 5, 5]], 6, 7, 8]
print(c, d, e, f, g)
