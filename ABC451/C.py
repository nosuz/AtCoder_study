#!/usr/bin/python3

# C - Understory
# https://atcoder.jp/contests/abc451/tasks/abc451_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
5
1 5
1 7
1 8
2 7
1 3
<expected> 1
2
3
1
2

12
2 256601193
1 85138616
1 202564041
2 276477192
1 55551662
1 170271057
2 754166580
1 854388209
1 772036624
2 651124113
1 301137866
2 290875185
<expected> 0
1
2
0
1
2
0
1
2
2
3
3

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


def bin_search_left(target, lst):
    left = 0
    right = len(lst) - 1
    result = -1

    while right >= left:
        p = (right + left) // 2
        if target < lst[p]:
            right = p - 1
        elif target > lst[p]:
            result = p
            left = p + 1
        else:
            return p

    # targetより小さい要素の最大インデックス（なければ-1）
    return result

def bin_search_right(target, lst):
    left = 0
    right = len(lst) - 1
    result = -1

    while right >= left:
        p = (right + left) // 2
        if target < lst[p]:
            result = p
            right = p - 1
        elif target > lst[p]:
            left = p + 1
        else:
            return p

    # targetより大きい要素の最小インデックス（なければ-1）
    return result

Q = int(input())

trees = []
cut = 0
count = []
for _ in range(Q):
    command, height = map(int, input().split())
    # debug(f"c:{command},i:{index},{index_left},cut:{cut}")
    if command == 1:
        # 植える
        index = bin_search_right(height, trees, cut)
        if index == -1:
            trees.append(height)
        else:
            trees.insert(index+cut, height)
    else:
        # 切る
        index = bin_search_left(height, trees, cut)
        if index == -1:
            cut = 0
            trees = []
        else:
            cut = index+1
    debug(trees)

    count.append(len(trees) - cut)

print(*count)
