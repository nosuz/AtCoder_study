#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
8 3
1 5
1 8
2 4
<expected> 2

8 4
1 5
1 8
2 4
6 8
<expected> 3

5 10
2 5
1 5
1 2
2 4
2 3
1 3
1 4
3 5
3 4
4 5
<expected> 40

2 1
1 2
<expected> 0

3 1
1 2
<expected> 0
"""

import math
from collections import defaultdict

n, m = map(int, input().split())

grp = defaultdict(lambda: 0)
for _ in range(m):
    a, b = map(int, input().split())
    rad_a = 2 * math.pi * (a - 1) / n
    rad_b = 2 * math.pi * (b - 1) / n

    a_x = math.sin(rad_a)
    a_y = math.cos(rad_a)
    b_x = math.sin(rad_b)
    b_y = math.cos(rad_b)

    if a_x == b_x:
        slope = "inf"
    else:
        slope = math.floor((a_y - b_y) / (a_x - b_x) + 10 ** 7)
    # print(f"({a}, {b}) -> {slope}")
    grp[slope] += 1

print(grp)
if len(grp) == 0:
    print(0)
else:
    crossing = 0
    _m = m
    for v in grp.values():
        crossing += v * (_m - v)
        _m -= v
    print(crossing)
