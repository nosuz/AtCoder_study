#!/usr/bin/python3

# A - Black Square
# https://atcoder.jp/contests/abc441/tasks/abc441_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
3 3
5 10
<expected> Yes

5 5
10 1000
<expected> No

1 2
1 1
<expected> No

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


P, Q = map(int, input().split())
X, Y = map(int, input().split())

if (P <= X <= (P+99)) and (Q <= Y <= (Q+99)):
    print("Yes")
else:
    print("No")
