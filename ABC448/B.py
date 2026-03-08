#!/usr/bin/python3

# B - Pepper Addiction
# https://atcoder.jp/contests/abc448/tasks/abc448_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
7 5
4 4 8 3 7
1 2
2 3
5 2
4 10
2 3
5 4
2 3
<expected> 15

1 1
1
1 1
<expected> 1

15 10
7 94 100 82 63 81 75 2 76 73
10 44
5 77
10 47
7 32
2 82
5 90
3 37
6 70
6 28
3 25
2 26
10 56
1 69
5 46
7 26
<expected> 438

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, M = map(int, input().split())
# N: 料理の数
# M: コショウの種類
C = list(map(int, input().split()))
ans = 0
for _ in range(N):
    A, B = map(int, input().split())
    consume = min(B, C[A-1])
    C[A-1] -= consume
    ans += consume

print(ans)
