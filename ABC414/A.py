#!/usr/bin/python3

# A - Streamer Takahashi
# https://atcoder.jp/contests/abc414/tasks/abc414_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
5 19 22
17 23
20 23
19 22
0 23
12 20
<expected> 3

3 12 13
0 1
0 1
0 1
<expected> 0

10 8 14
5 20
14 21
9 21
5 23
8 10
0 14
3 8
2 6
0 16
5 20
<expected> 5

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, L, R = map(int, input().split())

count = 0
for _ in range(N):
    X, Y = map(int, input().split())

    if (X <= L) and (R <= Y):
        count += 1

print(count)
