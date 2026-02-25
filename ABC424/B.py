#!/usr/bin/python3

# B - Perfect
# https://atcoder.jp/contests/abc424/tasks/abc424_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
3 2 5
1 1
3 2
2 1
3 1
1 2
<expected> 3 1

2 2 2
1 1
2 2
<expected>

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)

N, M, K = map(int, input().split())

ok = [set() for _ in range(N)]
for _ in range(K):
    A, B = map(int, input().split())
    ok[A-1].add(B)
    if len(ok[A-1]) == M:
        print(A)
