#!/usr/bin/python3

# C - AtCoder Riko
# https://atcoder.jp/contests/abc444/tasks/abc444_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
4
10 5 5 10
<expected> 10 15

3
4 4 4
<expected> 4

6
10 187 344 100 434 257
<expected> 444

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
A = list(map(int, input().split()))

A.sort()

L = []
if len(A) % 2 == 0:
    # 全部割れてる
    l = 0
    for i in range(len(A)//2):
        if A[i] + A[N-i-1] != A[i + 1] + A[N-i-2]:
            break
        else:
            l = A[i] + A[N-i-1]
    else:
        if l > 0:
            L.append(l)

# 大きいのが残ってる
max_l = A[N-1]
B = [a for a in A if a < max_l]
if len(B) == 0:
    L.append(max_l)
elif len(B) % 2 == 0:
    l = 0
    n = len(B)
    for i in range(len(B)//2):
        if B[i] + B[n-i-1] != B[i + 1] + B[n-i-2]:
            break
        else:
            l = B[i] + B[n-i-1]
    else:
        if l > 0:
            L.append(l)
L.sort()
print(*L)
