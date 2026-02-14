#!/usr/bin/python3

# C - Sugoroku Destination
# https://atcoder.jp/contests/abc445/tasks/abc445_c

# python ../validate.py C_alt.py

"""TEST_DATA
7
2 4 7 5 5 6 7
<expected> 5 5 7 5 5 6 7

5
1 2 3 4 5
<expected> 1 2 3 4 5

15
11 3 10 7 15 10 10 11 11 13 11 12 14 14 15
<expected> 11 14 14 14 15 14 14 11 11 14 11 12 14 14 15

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    A[i] -= 1

stucked = [-1] * N
for i in range(N-1, -1, -1):
    if A[i] == i:
        stucked[i] = i
    else:
        stucked[i] = stucked[A[i]]

print(*[x+1 for x in stucked])
