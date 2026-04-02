#!/usr/bin/python3

# D - Transmission Mission
# https://atcoder.jp/contests/abc414/tasks/abc414_d

# python ../validate.py D.py

# pytest tests/test_d.py
# pytest tests/test_d.py -k sample1

"""TEST_DATA
7 3
5 10 15 20 8 14 15
<expected> 6

7 7
5 10 15 20 8 14 15
<expected> 0

7 1
5 10 15 20 8 14 15
<expected> 15

5 3
1 2 3 4 6
<expected> 2

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, M = map(int, input().split())
X = list(map(int, input().split()))
# 配列のpointerに便利
# X = list(map(lambda x: int(x) - 1, input().split()))

X.sort()
delta = [X[i] - X[i - 1] for i in range(1, N)]
delta.sort()
debug(delta)

# 距離が離れているところから順に切断する。
# if M == 1:
#     print(sum(delta))
# else:
#     # 局数が $M$ ならば、切断は $M - 1$
#     print(sum(delta[: -(M - 1)]))

# Or

# 逆に近い方の $N - M - 1$ をカバーする。
print(sum(delta[: N - M]))
