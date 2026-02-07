#!/usr/bin/python3

# A - Repdigit
# https://atcoder.jp/contests/abc444/tasks/abc444_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
444
<expected> Yes

160
<expected> No

999
<expected> Yes

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = input()

if N[0] == N[1] == N[2]:
    print("Yes")
else:
    print("No")
