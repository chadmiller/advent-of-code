#!/usr/bin/python3

exdoc = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

doc = """\
...#..............#.#....#..#..
...#..#..#..............#..#...
....#.#.......#............#...
..##.....##.........#........##
...#...........#...##.#...#.##.
..#.#...#....#.....#........#..
....##.###.....#..#.......#....
.#..##...#.....#......#..#.....
............##.#...#.#.....#.#.
..........#....#....#.#...#...#
..##....#.#.#......#.........#.
#.#.........#..............##..
....##.##......................
....##..#...........#..........
..#..#.#........##....#......#.
..............#..#....#.....#..
.............#...#.....#...#...
.#...........#..........#...#..
.#......#.......#......#.......
#..#.............#..#....##.###
........#.#...........##.#...#.
......#..#.....##......#.......
.....#.....#....#..............
#...##.#......#......#...#.....
...........................#...
...#....................#.....#
..#.....#...#.....##.....#.....
....................#......#..#
.......#.....##......##....#...
#........##...#.....##..#...#..
........#..#.#......#..###..#.#
##.....#.............#.#....#..
..#.................#....######
.#.#..#.....#.#..........#.#...
.........#....#...#............
........#..#.....#.............
............#.#.............##.
...#....#..#......#............
.##....#.....#...#.#...........
..#..............#...........##
.....#.#.##...#................
..........#..#.#..........##..#
..#....#...#...#.....######....
....#.#..#........#....#.###...
.......................#.......
..#.....#.##................#..
.....#......#..#.....#........#
.#...###.......#.#.........#..#
............#..................
..#.........##.........##......
#...........#.#.......###.#....
.#...#.....#.........###.....#.
.#............#........#..#....
...##.#......##................
........#...#...#...#..........
.......#.##......##.#..........
....##.......#..#....#....#....
......#.........###........#...
#....#....####....##......#....
......................#....#.#.
...#.#.#....#.#...#...#......#.
......#.....##.#...........###.
#........#.........##......#.#.
....##.....#.....#..#..........
......#...#...#.........#...##.
..#........#..................#
.........#..##.#..#..#...#.#..#
.....#.....#...#.....###.....##
.............#....#...#........
..........#.#.#...#..#...#....#
#...............##.......#.....
#...#.............#..#...#....#
..#...#...##...##...#..#.......
..#..#........#.#...........#..
.....#.....#..................#
....#....##....###..###...##...
..#......###.........##....#.##
.......#.##...#.......#..#.....
...#.#.#.#.....##..#..#........
................##....#.#......
..#...#...#...#.....##.#...#..#
..#..#.....#..##....#....#.....
.###...#......#........#.....##
##......#..#........#..........
....#...#..#....##..#......####
.#.....##....#..........#......
.#...#....#.........#...#....#.
.....#..#.#..#......#..##....#.
...#.##...#...#........#......#
.#..#...#.#..#.........#...#...
#....#......##.....#.......#...
..##............##..#.#.#...#..
##.......#.......##............
#......#.##........#...#...#...
.#.#.......##.........#..#.#...
.............##.#........#.....
.#..#...###...#..#.............
.....#...#..#....#.......#.....
#.#.........#.#.#...#...#.#....
.....#.......#.##.##...#....#..
.#.##..#.....#...#.#.#.#.#..#..
..........#...................#
.....#.#.#...##.........#..#..#
.#..#....##......#...#.........
.##......#......#...#........#.
.....##.#......#............#.#
.#.....##..#...........##......
.....#......#.......##....#....
..#..##..........#.#..........#
#.#.......##..#..##.#....#.....
.......#..#.#.......##......#.#
....#...##...#..............#..
.....#.........#......#...##...
#.........#........##..#.....#.
.#.#..#.....##.......#......#..
........#..#....#.....###..#...
#.#..#.#..........#............
..#......##..#....#.........#..
#..............................
.......#............#..#..#.#..
.#.....#.#....#..#.##.#........
.......#.###.#........##.#..#..
..............#....#.....##.#..
#..............#....#.###......
.#..#..#...###............#...#
.#.##...#....#..#...#...#......
......##..#..#......#..#....#..
.........#.......##............
...........##...#..#....####...
.#..................#..........
#...#..#..................#....
..............#.....##.....#...
..#.#..#...##..#.....#.....#..#
....#....#.#.........#.....#...
.#.......#...#....#...#.#..#..#
#.........##.....##.......#...#
#..#............#....#........#
..........##...#......#....#...
.......#..##...............#...
#............#.#.#.....#.......
.#........##...#...............
..##....#.....#..#.##.#......#.
.#...#.............#...#.....#.
...##....#.......#......#.#..#.
#......................#..#.##.
...#..........#..#.........#...
..#......#.......#.#....#......
....#............#...#......#..
.....#..#..##...#...#.........#
.....#......#....#....#........
.............#..#..........#...
....#..............#.....#.#...
....#.................#.#...#.#
.........#.#...........###.#.##
#...........#..##.#....#.##.#..
#.#.....#......................
##.#.........#....##.#.#..#.#..
#..........#.#.#.#.#..#..##..#.
..#...#..###.........#......#..
.....#......#..#.#............#
...........#...#.#.#.###....#..
#....#..#.......##.#.......##..
..............#.....##.#.......
.#.....#.#..#.........#.#.#..#.
..#..#..#..#................#..
...........#..#.#...#.........#
.#..#..#...#........#...#.#..#.
...#.#..#......#..#............
........#......##.....#....#...
#...#......##.#.#..............
.#........................#....
#.#.....#.##.....#..#.#........
#..........##.#.......#....#..#
#...#..#..#.....#....#....#....
#...........#..#.#....##.##....
##......#..#........#.......##.
#........#..#...#..........#...
...#...#......##....#.#........
...##..#..#.##....#...#........
#.#..#....#...#........#.......
..........#.......#..........#.
......##...#....###...#....#...
........#..#.....#......#......
....#.........##...#..##......#
....#...........#.#..#.#.#.#..#
..#......#..#......#........#.#
#..#....#.....#.............#..
............................#..
#...#.#.....#...#....#....#....
........#...#...#...#...#......
.###........#....#.##.....##.#.
.........#.....#..........#....
.#.........#....##.#.....#.....
#..#....................##.#...
..##.#.............#....#.#....
..#.#........#............##.#.
#........#...##.....#...#.....#
.........#.#..........#....#..#
...###.#..#.#......#.#.....#...
......#.....#..#...#........#..
.......#...#.....#....#....#..#
.#.#........#......##.......#..
#.................###..........
#........#.#..#....#..#........
..##....#.#...##...#...##....#.
...#.#......##...#.....#..#....
#..#........#...###....#.......
##.#....#..#.#..........#......
....#...###...#.....#........#.
..#.#........#....##.#.........
......##.##.................##.
.#....##...#.#..#.#............
.#...###........#......#.......
##..#.#......#..#..#...#.......
.......##..#....#........#....#
......#..........#.............
....##..##..#......#.#.........
.....#....................##...
...###.....#.....#...#.#.##.#..
....#.#..#.......#..#......##..
.......#.#..#.##.#...#......#..
...#.#....#.#...#..##...#...#..
#.##...#....#..#.............#.
...#...#...#.......#..........#
.#..#.............#..##.#......
....#.......#..............#.#.
..................#..#.....##.#
.#...#..#......#..........#...#
..#.#.....#..#....#....#####.#.
.......###.......#....#....#...
......#.#........#...#.........
......#..#.#.#....#.#.#....##..
.#...#.#...##.#......#.........
#....#..##....#.#.......#....#.
..##.#.....#.....#.........#...
......#......#....#....#.....#.
...##.....#....#......#......#.
......#......##............#.#.
.##.#.......#....#...#....#....
....#..#..#...##.......#..#....
....#....#...#.#........#..#...
....#.....#..........#..#......
....#....#...#.....#..##.....#.
##...#..##......#....##..#..#..
.....##.##..............##.....
#.#....#.##..#....#...##.......
..#.....##.....#.....######...#
...#.....#.#.#......#......##.#
...........##.............#....
...##......#..#......#...#.....
....#.##......#..#....#.#..#...
.#..#....#...#..#.....##.......
.....#..#.................#..#.
................#..#...#......#
...##....#.....#..#....##......
....##...............##...#....
......#..........#..##.........
.......###.......#.........#..#
......................#....#.#.
#.#.....#...##............#....
........#......##......#.....#.
...#....#....#.#..##.#..#.#.#..
..#.#....#.##...#..#.....#.#...
............#....#..#.......#..
#...#...#.#......#...##.....#.#
......#....#....#.......#......
....#.......#..........#....#..
........#####........#....#....
......#....##..............#.#.
....#....#.......#.......#.....
.##.#....##....#...............
#.....##........#..#.#...#.#...
...#......##....#..............
.#.....#.....#.......##....##..
#....#..........#.#..#.........
......##..........##.......#...
.##......##.....#.#....#......#
....#......................#...
.#...........###........#...#..
#.#..#..#..#...##.#....#.#..#..
...##...........#.#..........#.
......#.#..#....#....#.........
....#....#.#......#.........##.
.#..#...#...##....#...#......#.
#.#......#...#.#.#...........#.
##.....#..........##....##..##.
...#.#.....#..##........#......
..#........##........#..#......
.......#...............##..#...
.......#.#....#..###...........
.............#........#...#....
#.................#......#..#..
...#....#..#..............#...#
.............#....##....#..##..
#........#..........##...##...#
............#....#.....#.#....#
.....#..............##..#...#..
..#....#......###....#.#...##..
....##......#.....#....#.......
.....#...............#.....#...
.#.....#.....#..............#..
#................#..#..........
.##....#....#.....#............
#.####...#..#..#....#..........
..##........##.....##......#..#
......#.....#...##.........##..
....##..#.....#.#.........#...#
.....##..#....#....#.#...#..#..
...#............#...........#..
.......#.#..#.#.#..#........#.#
....#.#........#.#.#..#...#...#
..#....#....#..#......#........
.#...........................#.
.#..#....####........##......#.
.#.....#..#.#.................#
.#..#...........#...#....#...#.
......##..#........#..#....#...
..#.............#....#........#
#.#..........#.##.......#.#..#.
..#....#...#...............#...
..............#..........#..#..
..#.....#.#.....#...#...#..#...
.........#...###.#...#........#"""

forest = doc.split("\n")

l = len(forest)
w = len(forest[0])

xinc = 3
yinc = 1

count = 0
pos = 0, 0
while pos[1] < len(forest):
    pos = pos[0]+xinc, pos[1]+yinc

    if pos[1] > len(forest)-1:
        print(xinc, yinc, "hit", count, "trees")
        break

    if forest[pos[1]][pos[0]%w] != ".":
        count += 1

