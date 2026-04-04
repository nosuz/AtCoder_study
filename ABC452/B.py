#!/usr/bin/python3

# B - Draw Frame
# https://atcoder.jp/contests/abc452/tasks/abc452_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
4 5
<expected> #####
#...#
#...#
#####

5 6
<expected> ######
#....#
#....#
#....#
######

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


H, W = map(int, input().split())

for h in range(H):
    if h == 0 or h == (H - 1):
        for _ in range(W):
            print("#", end="")
        print()
    else:
        for w in range(W):
            if w == 0 or w == (W - 1):
                print("#", end="")
            else:
                print(".", end="")
        print()
