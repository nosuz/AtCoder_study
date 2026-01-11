#!/usr/bin/python3

# A - Octave
# https://atcoder.jp/contests/abc440/tasks/abc440_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
110 2
<expected> 440

233 3
<expected> 1864

432 1
<expected> 864

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


X, Y = map(int, input().split())

print(X * (2**Y))
