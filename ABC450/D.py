#!/usr/bin/python3

# D - Minimize Range
# https://atcoder.jp/contests/abc450/tasks/abc450_d

# python ../validate.py D.py

# pytest tests/test_d.py
# pytest tests/test_d.py -k sample1

"""TEST_DATA
3 10
3 21 9
<expected> 4

5 6
4 100 5 10 450
<expected> 2

3 10
3 4 9
<expected> 5

3 10
5 4 9
<expected> 5

3 4
2 3 4
<expected> 2

5 10
3 4 5 6 7
<expected> 4

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, K = map(int, input().split())
A = list(map(int, input().split()))

mods = [A[i] % K for i in range(N)]
mods.sort()
debug(mods)

# 先頭と最後の間隔が最大と仮定する。
# その場合は、今の配列が最もコンパクト
max_gap = mods[0] - (mods[-1]-K)
max_a = mods[-1]
min_a = mods[0]

# 間隔が最大の場所を探す。
for i in range(N-1):
    gap = mods[i+1] - mods[i]
    if gap > max_gap:
        max_a = mods[i]
        min_a = mods[i+1]-K
        max_gap = gap

print(max_a - min_a)
