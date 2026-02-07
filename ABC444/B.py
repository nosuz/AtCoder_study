#!/usr/bin/python3

# B - Digit Sum
# https://atcoder.jp/contests/abc444/tasks/abc444_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
30 4
<expected> 3

2026 10
<expected> 121

99999 45
<expected> 1

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, K = map(int, input().split())

answer = 0
for i in range(N+1):
    total = 0
    remain = i
    for d in [10000, 1000, 100, 10, 1]:
        total += remain // d
        remain = remain % d
    if total == K:
        answer += 1
print(answer)
