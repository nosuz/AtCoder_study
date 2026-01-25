#!/usr/bin/python3

# C - Peer Review
# https://atcoder.jp/contests/abc442/tasks/abc442_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
6 5
1 2
1 4
2 3
5 3
3 1
<expected> 0 1 0 4 4 10

7 3
1 2
3 4
5 6
<expected> 10 10 10 10 10 10 20

6 9
3 6
2 5
2 3
4 3
1 5
6 2
3 1
5 3
2 4
<expected> 1 0 0 1 0 1

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


def combination(n):
    # 3人選ぶので割り算の項が固定されて簡単になる。
    # n! / (n-3)! / 3!
    c = n * (n-1) * (n - 2) // 6
    return c


N, M = map(int, input().split())

conflict = [set() for i in range(N)]
for m in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1

    conflict[A].add(B)
    conflict[B].add(A)
# print(conflict)

for n in range(N):
    # print(conflict[n])
    # 著者も利害関係者に含まれるので、査読できない。
    reviewers = N - len(conflict[n]) - 1
    # print(reviewers)
    # 査読可能な人数から3人を選ぶ組み合わせの数。
    print(combination(reviewers))
