L = [1, 2, [3, 4], [5, 6, [7]]]

def flatten(L):
    for item in L:
        if isinstance(item, list):
            yield from flatten_list(item)
        else:
            yield item

flatten(L)