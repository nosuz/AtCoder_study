#!/usr/bin/python3

# C - Truck Driver
# https://atcoder.jp/contests/abc430/tasks/abc430_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
11 4 2
abbaaabaaba
<expected> 3

13 1 2
bbbbbbbbbbbbb
<expected> 0

2 1 2
ab
<expected> 2


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, A, B = map(int, input().split())
S = list(input())

result = 0
ia = 0
ib = 0
count_a = 0
count_b = 0
for i in range(N):
    # Aを満たす右端を探す
    # ここから左はすべてAを満たす
    while (ia < N) and (count_a < A):
        if S[ia] == 'a':
            count_a += 1
        ia += 1

    # Bを満たす右端を探す
    # ここから左はBを満たすのでダメ
    while (ib < N) and (count_b < B):
        if S[ib] == 'b':
            count_b += 1
        ib += 1

    if count_a >= A:
        if count_b < B:
            # Bを満たす右端を探したのにBを満たせない
            # ということは、右端に達した
            result += N - ia + 1
        elif ib > ia:
            # Bを満たす。だだし、その場所が
            # Aを満たす位置よりも手前に無いことを確認
            result += ib - ia

    # 右端を一つ進める
    if S[i] == 'a':
        count_a -= 1
    else:
        count_b -= 1
    i += 1

print(result)
