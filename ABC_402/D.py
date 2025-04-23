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

8 2
1 8
2 7
<expected> 0
"""

from collections import defaultdict

n, m = map(int, input().split())

# mod = n / 2

grp = defaultdict(lambda: 0)
for _ in range(m):
    a, b = map(int, input().split())
    # ab = ((a + b) / 2) % mod
    ab = (a + b) % n  # no need to divide by 2
    # ab = ((a + b - 2) / 2) % mod # = ((a - 1 + b - 1) / 2) % mod
    # print(f"({a}, {b}) -> {ab}")
    grp[ab] += 1

# print(grp)
crossing = 0
_m = m
for v in grp.values():
    crossing += v * (_m - v)
    _m -= v
print(crossing)
