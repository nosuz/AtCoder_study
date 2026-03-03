#!/usr/bin/python3

# B - N - 1
# https://atcoder.jp/contests/abc429/tasks/abc429_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
4 10
3 2 3 4
<expected> Yes

5 16
3 3 4 2 5
<expected> No

6 16
0 8 0 2 6 8
<expected> Yes

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, M = map(int, input().split())
A = list(map(int, input().split()))

total_sum = sum(A)

for i in range(N):
    if (total_sum - A[i]) == M:
        print("Yes")
        break
else:
    # No break
    print("No")
