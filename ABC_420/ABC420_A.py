#!/usr/bin/python3

# python3 validate.py sample.py

# A - What month is it?
# https://atcoder.jp/contests/abc420/tasks/abc420_a

"""TEST_DATA
5 9
<expected> 2

1 1
<expected> 2

12 12
<expected> 12


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


X, Y = map(int, input().split())

ans = (X + Y) % 12
if ans == 0:
    print(12)
else:
    print(ans)
