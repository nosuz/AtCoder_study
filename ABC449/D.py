#!/usr/bin/python3

# D - Make Target 2
# https://atcoder.jp/contests/abc449/tasks/abc449_d

# python ../validate.py D.py

# pytest tests/test_d.py
# pytest tests/test_d.py -k sample1

"""TEST_DATA
-4 3 1 3
<expected> 10

-14 14 -14 14
<expected> 449

"""

import os


def black_count(x, y):
    count = 0
    if (y % 2) == 0:
        # 偶数
        if x <= y:
            count += x + 1  # 0 上を含む
        else:
            count += y+1
            count += (x - y) // 2
    else:
        # 奇数
        if x > y:
            count += (x - y + 1) // 2
        else:
            # 全て 0
            pass
    return count


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


L, R, D, U = map(int, input().split())

count = 0
if L == 0 == R:
    for i in range(D, U+1):
        if (abs(i) % 2) == 0:
            count += 1
elif L < 0 < R:
    L_abs = abs(L)
    R_abs = abs(R)
    # 左右を数える
    for i in range(D, U+1):
        i_abs = abs(i)
        debug(f"i:{i}", black_count(L, i), black_count(R, i))
        count += black_count(L_abs, i_abs)
        count += black_count(R_abs, i_abs)
        # 重なる 0 の部分を引く
        if (i_abs % 2) == 0:
            count -= 1
elif 0 == L < R:
    R_abs = abs(R)
    # 右を数える
    for i in range(D, U+1):
        i_abs = abs(i)
        count += black_count(R_abs, i_abs)
elif L < 0 == R:
    L_abs = abs(L)
    # 左を数える
    for i in range(D, U+1):
        i_abs = abs(i)
        count += black_count(L_abs, i_abs)
elif L <= R < 0:
    L_abs = abs(L)
    R_abs = abs(R)
    # L から R を引く
    for i in range(D, U+1):
        i_abs = abs(i)
        count += black_count(L_abs, i_abs)
        count -= black_count(R_abs - 1, i_abs)
elif 0 < L <= R:
    L_abs = abs(L)
    R_abs = abs(R)
    # R から L を引く
    for i in range(D, U+1):
        i_abs = abs(i)
        count += black_count(R_abs, i_abs)
        count -= black_count(L_abs - 1, i_abs)
else:
    # 考慮漏れがある。(debug)
    raise

print(count)
