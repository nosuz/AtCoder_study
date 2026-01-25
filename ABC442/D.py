#!/usr/bin/python3

# D - Swap and Range Sum
# https://atcoder.jp/contests/abc442/tasks/abc442_d

# python ../validate.py D.py

# pytest tests/test_d.py
# pytest tests/test_d.py -k sample1

"""TEST_DATA
4 4
2 7 1 8
1 2
2 1 2
1 1
2 2 4
<expected> 3
17

8 10
22 75 26 45 72 81 47 29
2 2 7
2 6 8
2 4 4
1 2
2 1 3
1 1
2 2 4
1 2
1 4
2 1 1
<expected> 346
157
45
123
142
26

8 2
22 75 26 45 72 81 47 29
1 2
2 1 3
<expected> 123

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, Q = map(int, input().split())

A = list(map(int, input().split()))
# print(A)
sum = [0]
for n in range(N):
    sum.append(sum[n] + A[n])
# print(sum)

# Qの制約から、実際に操作しても間に合うと判断した。
for q in range(Q):
    query = list(map(int, input().split()))
    # print(query)
    if query[0] == 1:
        x = query[1] - 1
        # 累積和は、隣と交換しても前後に影響しない。
        delta = A[x+1] - A[x]
        sum[x+1] += delta
        # 移動
        tmp = A[x+1]
        A[x+1] = A[x]
        A[x] = tmp
    else:
        # print(A)
        # print(sum)
        l = query[1] - 1
        r = query[2]
        print(sum[r] - sum[l])
