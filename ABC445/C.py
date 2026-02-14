#!/usr/bin/python3

# C - Sugoroku Destination
# https://atcoder.jp/contests/abc445/tasks/abc445_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

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

4
2 3 4 1
<expected> 1 2 3 4

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
A = list(map(int, input().split()))

# reverse pathは、複数の経路があることに注意
rev_path = [[] for _ in range(N)]
stuck = set()
stucked = [-1] * N
for i in range(N):
    A[i] -= 1
    if A[i] == i:
        stuck.add(i)
        stucked[i] = i
    else:
        rev_path[A[i]].append(i)
debug(stuck, rev_path)

for s in stuck:
    que = rev_path[s]
    while len(que) > 0:
        i = que.pop()
        stucked[i] = s

        que += rev_path[i]

print(*[x+1 for x in stucked])
