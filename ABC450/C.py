#!/usr/bin/python3

# C - Puddles
# https://atcoder.jp/contests/abc450/tasks/abc450_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
5 15
##########..###
#...#######.###
####....###..##
######.########
########....###
<expected> 2

10 22
######################
####.#################
###...################
##.###.##.....########
##.....##.####.#######
.######.#......#.....#
.######.#.####.#.#####
#########.....##.#####
################.#####
################.....#
<expected> 4

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)

def make_neighbor(H, W, pos):
    neighbor = []
    for h,w in [(1,0), (-1,0), (0,1), (0,-1)]:
        if (0 <= (pos[0]+h) < H) and (0 <= (pos[1]+w) < W):
               neighbor.append((pos[0]+h, pos[1]+w))
    return neighbor

def paint_dot(h, w):
    global map

    # `#`で囲まれたエリアかのフラグ
    closed_area = True
    stack = [(h,w)]
    # 深さ優先探索で`.`を消す。
    while len(stack) > 0:
        pos = stack.pop()
        if map[pos[0]][pos[1]] == '#':
            continue

        map[pos[0]][pos[1]] = '#'

        neighbors = make_neighbor(H, W, pos)
        if len(neighbors) < 4:
            # mapからはみ出したということは、閉じていない
            closed_area = False
        for neighbor in neighbors:
            if map[neighbor[0]][neighbor[1]] == '.':
                stack.append(neighbor)

    return closed_area

H, W = map(int, input().split())

map = []
for _ in range(H):
    map.append(list(input()))
# debug(map)

stack = []
count = 0
for h in range(1, H-1):
    for w in range(1, W-1):
        if map[h][w] == '.':
            # 深さ優先探索で見つけた場所に連なるエリアを塗りつぶす
            closed_area = paint_dot(h, w)
            if closed_area:
                count += 1

print(count)
