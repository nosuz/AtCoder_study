#!/usr/bin/python3

# python3 validate.py sample.py

# C - King's Summit
# https://atcoder.jp/contests/abc419/tasks/abc419_c

"""TEST_DATA
3
2 3
5 1
8 1
<expected> 3

5
6 7
6 7
6 7
6 7
6 7
<expected> 0

6
91 999999986
53 999999997
32 999999932
14 999999909
49 999999985
28 999999926
<expected> 44


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())

min_x = 10 ** 9
max_x = 0
min_y = 10 ** 9
max_y = 0
persons = []
for _ in range(N):
    x, y = map(int, input().split())
    persons.append((x, y))

    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

debug("min_x:", min_x, "max_x:", max_x, "min_y:", min_y, "max_y:", max_y)

mean_x = (min_x + max_x) // 2
mean_y = (min_y + max_y) // 2

max_distance = 0
for x, y in persons:
    delta_x = abs(x - mean_x)
    delta_y = abs(y - mean_y)
    if delta_x > delta_y:
        distance = delta_x
    else:
        distance = delta_y

    if distance > max_distance:
        max_distance = distance
print(max_distance)
