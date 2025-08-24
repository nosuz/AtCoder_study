#!/usr/bin/python3

# python3 validate.py sample.py

# C - Sum of Min Query
# https://atcoder.jp/contests/abc420/tasks/abc420_c

"""TEST_DATA
4 3
3 1 4 1
2 7 1 8
A 2 3
B 3 3
A 1 7
<expected> 7 9 9

1 3
1
1000000000
A 1 1
A 1 1
A 1 1
<expected> 1 1 1

5 3
100 100 100 100 100
100 100 100 100 100
A 4 21
A 2 99
B 4 57
<expected> 421 420 420


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, Q = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

total = 0
C = [0] * N
for i in range(N):
    if A[i] < B[i]:
        total += A[i]
        C[i] = A[i]
    else:
        total += B[i]
        C[i] = B[i]
debug(total)

for _ in range(Q):
    query = input().split()

    index = int(query[1]) - 1
    value = int(query[2])

    if query[0] == 'A':
        A[index] = value
    else:
        B[index] = value

    total -= C[index]
    if A[index] < B[index]:
        total += A[index]
        C[index] = A[index]
    else:
        total += B[index]
        C[index] = B[index]

    print(total)
