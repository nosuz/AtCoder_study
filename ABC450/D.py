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

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, K = map(int, input().split())
A = list(map(int, input().split()))

max_a = max(A)
# th以下ならば、max_aを超えないほうが良い。
th = K // 2

delta_less = []
delta_more = []
has_eqaul = False
for i in range(N):
    mod = (max_a - A[i]) % K
    mod_alt = K - mod
    debug(f"-A:{A[i]}, less:{mod}, more:{mod_alt}")
    if mod == 0:
        # ピッタリ
        continue

    if mod == mod_alt:
        # 同じ時は特別扱い
        has_eqaul = True
        continue

    if mod <= th:
        # 超えないほうが有利
        delta_less.append(mod)
    else:
        # 超えたほうが有利
        delta_more.append(mod_alt)
debug(delta_less, delta_more)

# moreとlessで最悪の値を探す
if len(delta_less) == 0:
    max_less =0
else:
    max_less = max(delta_less)

if len(delta_more) == 0:
    max_more =0
else:
    max_more = max(delta_more)

if has_eqaul:
    # どっちに付いたほうが有利か？
    if max_less > max_more:
        max_less = th # equalになる時は、偶数でthと等しい
    else:
        max_more = th
print(max_less + max_more)
