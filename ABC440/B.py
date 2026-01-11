#!/usr/bin/python3

# B - Trifecta
# https://atcoder.jp/contests/abc440/tasks/abc440_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
4
100 110 105 95
<expected> 4 1 3

8
72 74 69 70 73 75 71 77
<expected> 3 4 7

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
T = []
for i, t in enumerate(map(int, input().split())):
    T.append((i, t))

T.sort(key=lambda x: x[1])
print(T[0][0]+1, T[1][0]+1, T[2][0]+1)
