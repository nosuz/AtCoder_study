#!/usr/bin/python3

# python3 validate.py sample.py

# B - Search and Delete
# https://atcoder.jp/contests/abc417/tasks/abc417_b

"""TEST_DATA
8 5
1 2 2 3 3 3 5 6
2 2 7 3 2
<expected> 1 3 3 5 6

1 2
1
1 1
<expected>


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in B:
    for j in range(len(A)):
        if i == A[j]:
            A.pop(j)
            break
print(*A)
