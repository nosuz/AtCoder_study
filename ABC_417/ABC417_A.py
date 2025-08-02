#!/usr/bin/python3

# python3 validate.py sample.py

# A - A Substring
# https://atcoder.jp/contests/abc417/tasks/abc417_a

"""TEST_DATA
7 1 3
atcoder
<expected> tco

1 0 0
a
<expected> a

20 4 8
abcdefghijklmnopqrst
<expected> efghijkl


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, A, B = map(int, input().split())
S = input()

if B == 0:
    print(S[A:])
else:
    print(S[A:-B])
