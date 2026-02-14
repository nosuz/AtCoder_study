#!/usr/bin/python3

# C - AtCoder AAC Contest
# https://atcoder.jp/contests/abc422/tasks/abc422_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
5
3 1 2
100 0 0
1000000 1000000 1000000
31 41 59
1000000000 10000 1
<expected> 2
0
1000000
31
1

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


T = int(input())
for _ in range(T):
    N = list(map(int, input().split()))

    A = N[0]
    B = N[1]
    C = N[2]

    count = 0
    if C != 0:
        min_n = min(A, B, C)
        count += min_n
        A -= min_n
        C -= min_n

    # print(f"A:{A}, C:{C}")
    if (A > 0) and (C > 0):
        # print(f"min:{min(A, C, (A+C)//3)}")
        count += min(A, C, (A+C)//3)

    print(count)
