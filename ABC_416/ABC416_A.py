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
S = list(input())

debug(S, L-1, R)
span = set(S[L-1:R])

debug(span)
if (len(span) == 1) and 'o' in span:
    print("Yes")
else:
    print("No")
