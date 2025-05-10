#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
3 4
...E
.#..
....
<expected> >>>E ^#>^ >>>^

3 2
##
##
##
<expected> ## ## ##

7 20
....................
..#..#..####..#E##..
..#..#..#..#..#.....
..E###..#..#..####..
.....#..#..E.....#..
.....#..####..####..
....................
<expected> >v<<<<<>>>>>>>>v<<<< >v#^<#^^####v^#E##vv >v#^<#v^#>v#vv#^<<<< >>E###vv#>v#vv####^< >>^<<#vv#>>E<<<<<#^< >>^<<#vv####^<####^< >>^<<<<<>>>>^<<<<<^<


"""

h, w = map(int, input().split())

map = []
for _ in range(h):
    s = list(input())
    map.append(s)

# print(map)
next_pos = []
for y in range(h):
    for x in range(w):
        if map[y][x] == 'E':
            next_pos.append((y, x))
# print(next_pos)

while len(next_pos):
    this_pos = next_pos
    next_pos = []
    for pos in this_pos:
        # upper
        y = pos[0] - 1
        x = pos[1]
        if 0 <= y < h and 0 <= x < w:
            if map[y][x] == '.':
                map[y][x] = 'v'
                next_pos.append((y, x))

        # down
        y = pos[0] + 1
        x = pos[1]
        if 0 <= y < h and 0 <= x < w:
            if map[y][x] == '.':
                map[y][x] = '^'
                next_pos.append((y, x))

        # right
        y = pos[0]
        x = pos[1] + 1
        if 0 <= y < h and 0 <= x < w:
            if map[y][x] == '.':
                map[y][x] = '<'
                next_pos.append((y, x))

        # left
        y = pos[0]
        x = pos[1] - 1
        if 0 <= y < h and 0 <= x < w:
            if map[y][x] == '.':
                map[y][x] = '>'
                next_pos.append((y, x))

for y in range(h):
    print("".join(map[y]))
