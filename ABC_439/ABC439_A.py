#!/usr/bin/python3

# python3 validate.py sample.py

# A - 2^n - 2*n
# https://atcoder.jp/contests/abc439/tasks/abc439_a

"""TEST_DATA
1
<expected> 0

2
<expected> 0

11
<expected> 2026


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())

print(2**N - 2*N)
