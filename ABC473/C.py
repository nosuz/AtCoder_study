#!/usr/bin/python3

# C - Change Schools
# https://atcoder.jp/contests/abc473/tasks/abc473_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
8 5
3 3 5 5 4 4 3 2
<expected> 3

6 1
1 1 1 1 1 1
<expected> 1

14 8
6 1 5 3 8 4 3 4 3 5 1 2 5 1
<expected> 4

"""

import bisect
import os


# remove or comment out `debug()` before upload.
# the cost is not negligible
def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


# N: 人数
# K: class数
N, K = map(int, input().split())

A = list(map(int, input().split()))

klass = [0] * K

for p in A:
    klass[p - 1] += 1
klass.sort()
max = klass[-1]

debug(klass)
smallest_class = bisect.bisect_left(klass, max - 1)
print(K - smallest_class)
