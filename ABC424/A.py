#!/usr/bin/python3

# A - Isosceles
# https://atcoder.jp/contests/abc424/tasks/abc424_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
4 2 4
<expected> Yes

3 4 5
<expected> No

10 10 10
<expected> Yes

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)

A, B, C = map(int, input().split())

if (A == B) or (B==C) or (C==A):
    print("Yes")
else:
    print("No")
