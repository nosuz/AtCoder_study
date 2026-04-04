#!/usr/bin/python3

# python3 validate.py sample.py

# C - Flush
# https://atcoder.jp/contests/abc418/tasks/abc418_c

"""TEST_DATA
4 5
4 1 8 4
1
8
5
2
10
<expected> 1 17 14 5 -1

5 3
13 13 13 13 2
5
12
13
<expected> 19 47 51

2 1
2 3
2
<expected> 3


"""

import os
from bisect import bisect_left


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
debug(A)

total = 0
sums = [0]
for i in range(0, N):
    total = A[i] + total
    sums.append(total)
debug(sums)

for _ in range(Q):
    B = int(input())
    p = bisect_left(A, B)
    debug(f"p:{p}")

    if p == N and B > A[-1]:
        print(-1)
        continue

    ans = sums[p] + (N - p) * (B - 1) + 1
    print(ans)
