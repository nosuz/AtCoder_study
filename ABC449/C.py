#!/usr/bin/python3

# C - Comfortable Distance
# https://atcoder.jp/contests/abc449/tasks/abc449_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
6 2 4
aabcba
<expected> 2

9 3 6
aaaaaaaaa
<expected> 18

10 2 6
aabbccaabb
<expected> 6

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, L, R = map(int, input().split())
# 0始まりに補正
S = input()

bucket = dict()
for i in range(R+1):
    if i >= N:
        break

    if not S[i] in bucket:
        bucket[S[i]] = 0

    if i < L:
        continue

    bucket[S[i]] += 1

count = 0
for i in range(N):
    debug(S[i], bucket)
    if bucket[S[i]] > 0:
        count += bucket[S[i]]

    # update bucket
    if L < N:
        bucket[S[L]] -= 1
    if R < (N-1):
        if not S[R+1] in bucket:
            bucket[S[R+1]] = 0
        bucket[S[R+1]] += 1
    L += 1
    R += 1

print(count)
