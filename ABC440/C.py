#!/usr/bin/python3

# C - Striped Horse
# https://atcoder.jp/contests/abc440/tasks/abc440_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
4
8 2
1 10 10 1 1 10 10 1
8 3
1 10 10 1 1 10 10 1
8 4
1 10 10 1 1 10 10 1
4 100
100000 100000 100000 100000
<expected> 4
12
22
0

1
8 2
1 10 10 1 1 10 10 1
<expected> 4

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


T = int(input())

for _ in range(T):
    N, W = map(int, input().split())
    C = list(map(int, input().split()))

    if N <= W:
        print(0)
    else:
        W2 = 2 * W
        cost = [0] * W2
        for i in range(N):
            cost[i % W2] += C[i]
        debug(cost)

        sum = 0
        for i in range(W):
            sum += cost[i]
        lowest = sum
        # debug(lowest)
        for i in range(W, W2+W):
            sum += cost[i % W2] - cost[(i-W) % W2]
            debug(f"({i}, {i-W} => {sum})")
            if lowest > sum:
                lowest = sum
        print(lowest)
