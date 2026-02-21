#!/usr/bin/python3

# C - Omelette Restaurant
# https://atcoder.jp/contests/abc446/tasks/abc446_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
3
3 1
7 2 3
1 3 2
3 2
7 2 3
1 3 2
2 1
2 1
1 2
<expected> 3
5
0

1
3 1
7 2 3
1 3 2
<expected> 3

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


T = int(input())
for _ in range(T):
    # N: 最後の日
    # D: 期限
    # A: 納品個数
    # B: 消費個数
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 消費index
    item_at = 0

    # 消費
    for d in range(N):
        consume = B[d]
        while (consume > 0):
            if A[item_at] > consume:
                A[item_at] -= consume
                consume = 0
                # 期限チェック
                if (d - item_at) >= D:
                    A[item_at] = 0
                    item_at += 1
            else:
                consume -= A[item_at]
                A[item_at] = 0
                item_at += 1
    print(sum(A))
