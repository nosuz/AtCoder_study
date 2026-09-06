#!/usr/bin/python3

# A - Second Half Sum
# https://atcoder.jp/contests/abc473/tasks/abc473_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
8
1 3 7 8 4 2 5 6
<expected> 17

2
1 100
<expected> 100

10
31 41 59 26 53 58 97 93 23 84
<expected> 355

"""

import os


# remove or comment out `debug()` before upload.
# the cost is not negligible
def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())

A = list(map(int, input().split()))

mid = N // 2  # Nは、偶数
print(sum(A[mid:]))
