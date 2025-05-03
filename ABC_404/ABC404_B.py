#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
4
###.
..#.
..#.
..#.
...#
...#
###.
....
<expected> 2

13
.#..###..##..
#.#.#..#.#.#.
#.#.###..#...
###.#..#.#.#.
#.#.###..##..
.............
..#...#....#.
.##..#.#..##.
#.#..#.#.#.#.
####.#.#.####
..#..#.#...#.
..#...#....#.
.............
.............
.#....#...#..
.#...#.#..#..
####.#.#.####
.#.#.###..#.#
.##....#..##.
.#....#...#..
.............
..##..###.#.#
.#.#.#..#.###
.#.#..###.#.#
.#.#.#..#.#.#
..##..###..#.
<expected> 5


"""


def rotate_90(grid):
    n = len(grid)
    temp = [['' for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            temp[x][y] = grid[n - y - 1][x]
    # print(temp)
    return temp


n = int(input())

s = [None] * n
for i in range(n):
    s[i] = list(input())

t = [None] * n
for i in range(n):
    t[i] = list(input())

rotate = [0, 0, 0, 0]
mismatch = 0
for y in range(n):
    for x in range(n):
        if s[y][x] != t[y][x]:
            mismatch += 1
rotate[0] = mismatch

for i in range(3):
    s = rotate_90(s)
    mismatch = 0
    for y in range(n):
        for x in range(n):
            if s[y][x] != t[y][x]:
                mismatch += 1
    # print(f"rotete: {i}, miss: {mismatch}")
    rotate[i + 1] = mismatch + i + 1
# print(rotate)

min = n*n
for i in range(4):
    if min > rotate[i]:
        min = rotate[i]
print(min)
