#!/usr/bin/python3

# A - chmin
# https://atcoder.jp/contests/abc448/tasks/abc448_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
5 10
6 4 7 1 3
<expected> 1
1
0
1
0

1 1
1
<expected> 0

8 20
9 19 14 17 17 4 18 4
<expected> 1
0
0
0
0
1
0
0

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        X = A[i]
        print(1)
    else:
        print(0)
