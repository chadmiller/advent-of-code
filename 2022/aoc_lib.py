import re
import itertools
import heapq
import bisect
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
