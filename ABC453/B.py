#!/usr/bin/python3

# B - Sensor Data Logging
# https://atcoder.jp/contests/abc453/tasks/abc453_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
6 10
30 35 40 21 30 12 31
<expected> 0 30
2 40
3 21
6 31

"""

import os


# remove or comment out `debug()` before upload.
# the cost is not negligible
def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


T, X = map(int, input().split())
A = list(map(int, input().split()))

prev = 0
for i, a in enumerate(A):
    if (i == 0) or (abs(a - prev) >= X):
        print(f"{i} {a}")
        prev = a
