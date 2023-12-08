#!/usr/bin/python3

import re
import math
import itertools
import heapq
import bisect
from itertools import *
from functools import reduce, cache, lru_cache, cmp_to_key
from collections import Counter
from collections import defaultdict
from collections import deque
from collections import namedtuple
from numba import jit
from statistics import mean, median, median_low, median_high, mode, multimode

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
        for x, cell in enumerate(row):
            on_each(grid, cell, x, y, row[:x], row[x:], list(r[x] for r in grid[:y]), list(r[x] for r in grid[y:]))


def visit_each_neighbor(grid, x, y, on_each, skip_self=False):
   for jy in (y-1, y, y+1):
        for jx in (x-1, x, x+1):
            if jy < 0: continue
            if jy >= len(grid): continue
            if jx < 0: continue
            if jx >= len(grid[jy]): continue
            if skip_self and jx == x and jy == y: continue
            on_each(grid, jx, jy)

def get_word_at(row, offset, char_matcher):
    r"""
    >>> get_word_at("...abcdef..", 5, re.compile(r"\w"))
    (3, 'abcdef')
    >>> get_word_at("abcdef.....", 5, re.compile(r"\w"))
    (0, 'abcdef')
    >>> get_word_at(".....abcdef", 5, re.compile(r"\w"))
    (5, 'abcdef')
    """
    
    start = offset
    end = offset

    while start > 0 and char_matcher.match(row[start-1]) is not None:
        start -= 1

    while end < len(row)-1 and char_matcher.match(row[end+1]) is not None:
        end += 1

    return start, row[start:end+1]

def product(vals):
    if not vals:
        raise ValueError("zero values to product")
    return reduce((lambda a, b: a*b), vals, 1)


def poker_hand_key(hand, *ignored, cards=list(reversed("AKQJT98765432"))):
    """
    >>> poker_hand_key("Q5QQQ")
    [(4, 12), (1, 5)]
    >>> poker_hand_key("T55J5")
    [(3, 5), (1, 11), (1, 10)]
    >>> poker_hand_key("KK677")
    [(2, 13), (2, 7), (1, 6)]
    >>> poker_hand_key("32T3K")
    [(2, 3), (1, 13), (1, 10), (1, 2)]
    >>> poker_hand_key("KTJJT")
    [(2, 11), (2, 10), (1, 13)]
    >>> sorted("32T3K T55J5 KK677 KTJJT QQQJA".split(), key=poker_hand_key)
    ['32T3K', 'KTJJT', 'KK677', 'T55J5', 'QQQJA']
    >>> sorted("Q5QQQ JJJJJ KKKQJ KKKQQ KQQQQ".split(), key=poker_hand_key, reverse=True)
    ['JJJJJ', 'KQQQQ', 'Q5QQQ', 'KKKQQ', 'KKKQJ']
    >>> sorted("23456 789TJ".split(), key=poker_hand_key, reverse=True)
    ['789TJ', '23456']
    >>> sorted("77888 77788".split(), key=poker_hand_key, reverse=True)
    ['77888', '77788']
    """

    hand = sorted(hand, key=value_order.index)
    hand_grouped = list(list(g) for k, g in groupby(hand))

    return sorted(list((len(part), value_order.index(part[0])+2) for i, part in enumerate(hand_grouped)), reverse=True)



if __name__ == "__main__":
    import doctest
    doctest.testmod()

# vi: et smarttab ts=4 sw=4 :
