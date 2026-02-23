#!/usr/bin/python3

# D - Max Straight
# https://atcoder.jp/contests/abc446/tasks/abc446_d

# python ../validate.py D.py

# pytest tests/test_d.py
# pytest tests/test_d.py -k sample1

"""TEST_DATA
7
3 4 3 5 7 6 2
<expected> 4

5
5 4 3 2 1
<expected> 1

10
1 2 3 4 5 6 7 8 9 10
<expected> 10

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
A = list(map(int, input().split()))

# 最低の長さは1に注意
max_length = 1
steps = dict()

for i in range(N):
    a = A[i]
    if (a - 1) in steps:
        # ひとつ下がいる
        steps[a] = steps[a-1] + 1
        max_length = max(max_length, steps[a])
    else:
        # 自分より１つ下がいない
        steps[a] = 1

print(max_length)
