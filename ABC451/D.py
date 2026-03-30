#!/usr/bin/python3

# D - Concat Power of 2
# https://atcoder.jp/contests/abc451/tasks/abc451_d

# python ../validate.py D.py

# pytest tests/test_d.py
# pytest tests/test_d.py -k sample1

"""TEST_DATA
10
<expected> 21

69
<expected> 328

1099898
<expected> 819264512

"""

import os
from collections import deque


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())

# $10^9$未満の$2^n$を探しておく。意外と少ない。
# `str()`をできるだけ使わないようにtupleで管理しておく。
bin = []
candidate = set()
for i in range(0, 30):
    b = 2**i
    b_str = str(b)
    bin.append((b, len(b_str)))
    candidate.add(b)
debug(bin)

# 全ての組み合わせを探す。組み合わせは、1257874個しかない。
fifo = deque(bin)
while fifo:
    t = fifo.popleft()
    # debug(t)
    shift = 10 ** t[1]
    for q in bin:
        r = q[0] * shift + t[0]
        r_len = t[1] + q[1]
        if r_len > 9:
            # この後の数字は、同じ桁数かより桁数が大きい。
            # よってこの後は調べる必要がない。
            break
        # 既に見つかった数か調べなくても間に合う
        candidate.add(r)

        # 9桁未満ならば、もう一つ加えられる。
        if r_len < 9:
            fifo.append((r, r_len))
            # debug((r, r_len))
# debug(candidate)
debug(len(candidate))
lst = sorted(candidate)
print(lst[N - 1])
