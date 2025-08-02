#!/usr/bin/python3

# python3 validate.py sample.py

# C - Distance Indicators
# https://atcoder.jp/contests/abc417/tasks/abc417_c

"""TEST_DATA
9
3 1 4 1 5 9 2 6 5
<expected> 3

3
123456 123456 123456
<expected> 0

30
8 3 6 4 9 6 5 6 5 6 3 4 7 3 7 4 9 8 5 8 3 6 8 8 4 5 5 5 6 5
<expected> 17


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
A = list(map(int, input().split()))

count = 0
Aj = []
for j in range(N):
    a = j - A[j]
    if a > 0:
        Aj.append(a)
debug(Aj)

Ai_count = {}
for i in range(N):
    a = i + A[i]
    if a in Ai_count:
        Ai_count[a] += 1
    else:
        Ai_count[a] = 1
debug(Ai_count)

count = 0
for x in Aj:
    if x in Ai_count:
        count += Ai_count[x]
print(count)
