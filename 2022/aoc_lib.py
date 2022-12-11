import re
import itertools
import heapq
import bisect
from functools import reduce
from collections import Counter
from collections import defaultdict
from collections import deque
from collections import namedtuple
from numba import jit
from statistics import mean, median, median_low, median_high, mode, multimode

@jit(nopython=True)
def cmp(l, r):
    """
    >>> cmp("k", "b")
    1
    >>> cmp(5, 5)
    0
    """
    return (l > r) - (l < r)  # works because boolean is integery, t=1, f=0

def groups_of_n(source, n):
    """
    >>> list(groups_of_n("abcdef", 2))
    [('a', 'b'), ('c', 'd'), ('e', 'f')]
    >>> list(groups_of_n("abcdef", 3))
    [('a', 'b', 'c'), ('d', 'e', 'f')]
    """
    i = iter(source)
    while True:
        try:
            yield tuple(i.__next__() for nn in range(n))
        except RuntimeError:
            break

grid_deltas = ((0, -1), (-1, 0), (0, 1), (1, 0))

def visit_grid_cells(grid, on_each):
    for y, row in enumerate(grid):
        for x, cell in row:
            on_each(grid, x, y, row[:x], row[x:], list(r[x] for r in grid[:y]), list(r[x] for r in grid[y:]))

def product(vals):
    if not vals:
        raise ValueError("zero values to product")
    return reduce((lambda a, b: a*b), vals, 1)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
