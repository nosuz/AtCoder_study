#!/usr/bin/python3

# python3 validate.py sample.py

# https://atcoder.jp/contests/abc409/tasks/abc409_c

"""TEST_DATA
5 6
4 3 1 2
<expected> 2

4 4
1 1 1
<expected> 0

10 12
4 4 5 7 1 7 0 8 5
<expected> 13


"""

from collections import defaultdict

n, l = map(int, input().split())
d = list(map(int, input().split()))

points = defaultdict(lambda: 0)
points[0] = 1

# 余りを考える時は、0スタートが吉。
prev = 0
for x in d:
    y = (prev + x) % l
    points[y] += 1
    prev += x
# print(points)

# should 3の倍数
if (l % 3) != 0:
    print(0)
    exit()

total = 0
delta = l // 3
for i in range(0, delta):
    if (i in points) and ((i + delta) in points) and ((i + 2*delta) in points):
        # print(points[i], points[i + delta], points[i + 2*delta])
        total += points[i] * points[i + delta] * points[i + 2*delta]
print(total)
