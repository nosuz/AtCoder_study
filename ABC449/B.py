#!/usr/bin/python3

# B - Deconstruct Chocolate
# https://atcoder.jp/contests/abc449/tasks/abc449_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
7 9 5
2 4
1 3
2 1
2 1
1 3
<expected> 28
15
4
4
9

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


H, W, Q = map(int, input().split())

for _ in range(Q):
    type, RC = map(int, input().split())

    match type:
        case 1:
            # R
            print(RC * W)
            H -= RC
        case 2:
            # C
            print(RC * H)
            W -= RC
