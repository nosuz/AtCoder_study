#!/usr/bin/python3

# python3 validate.py sample.py

# A - Vacation Validation
# https://atcoder.jp/contests/abc416/tasks/abc416_a

"""TEST_DATA
10 6 8
xoxxooooxo
<expected> Yes

9 6 8
xoxxoxoox
<expected> No

1 1 1
x
<expected> No

1 1 1
o
<expected> Yes

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, L, R = map(int, input().split())
S = input()

debug(S, L-1, R)
for i in range(L-1, R):
    if S[i] != 'o':
        print("No")
        break
else:
    print("Yes")
