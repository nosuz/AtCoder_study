#!/usr/bin/python3

# B - Find Permutation 2
# https://atcoder.jp/contests/abc425/tasks/abc425_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
4
-1 -1 2 -1
<expected> Yes
3 1 2 4

5
-1 -1 1 -1 1
<expected> No

7
3 -1 4 -1 5 -1 2
<expected> Yes
3 7 4 1 5 6 2

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
A = list(map(int, input().split()))

candidate = set([i+1 for i in range(N)])

for a in A:
    if a > 0:
        if a in candidate:
            candidate.discard(a)
        else:
            break
else:
    # no break
    print("Yes")
    que = list(candidate)
    for i in range(N):
        if A[i] < 0:
            A[i] = que.pop()
    print(*A)
    exit()
print("No")
