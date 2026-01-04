#!/usr/bin/python3

# python3 validate.py sample.py

# C - 2026
# https://atcoder.jp/contests/abc439/tasks/abc439_c

"""TEST_DATA
10
<expected> 2 5 10

1
<expected> 0

50
<expected> 14 5 10 13 17 20 25 26 29 34 37 40 41 45 50


"""

import os
import math


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())

sqr = [0] * (N+1)

for x in range(1, int(math.sqrt(N))+1):
    x2 = x*x
    for y in range(x+1, int(math.sqrt(N))+1):
        x2y2 = x2 + y*y
        if x2y2 > N:
            break
        else:
            # debug(f"x: {x}, y: {y}")
            sqr[x2y2] += 1

# good = []
# for i in range(N+1):
#     if sqr[i] == 1:
#         good.append(i)
# good = [f"i: {i}, c: {c}" for i, c in enumerate(sqr) if c == 1]
good = [i for i, c in enumerate(sqr) if c == 1]

# debug(good)
print(len(good))
print(" ".join(map(str, good)))
