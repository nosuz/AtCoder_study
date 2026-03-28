#!/usr/bin/python3

# A - illegal
# https://atcoder.jp/contests/abc451/tasks/abc451_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
legal
<expected> Yes

atcoder
<expected> No

illegal
<expected> No

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)

S = input()

if (len(S) % 5) == 0:
    print("Yes")
else:
    print("No")
