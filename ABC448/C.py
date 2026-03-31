#!/usr/bin/python3

# C - Except and Min
# https://atcoder.jp/contests/abc448/tasks/abc448_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
6 6
3 2 5 9 1 2
2
4 5
5
1 2 3 4 6
3
2 5 6
4
1 2 5 6
1
5
3
1 2 3
<expected> 2
1
3
5
2
1

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, Q = map(int, input().split())
A = list(map(int, input().split()))

a_lst = []
for i, a in enumerate(A):
    a_lst.append((a, i))
# Kが最大でも5なので、先頭の6つを調べれば十分
a_sorted = sorted(a_lst)[:6]
debug(a_sorted)

for _ in range(Q):
    K = int(input())  # max. 5
    B = list(map(lambda x: int(x) - 1, input().split()))
    b_set = set(B)
    for a, i in a_sorted:
        if not i in b_set:
            print(a)
            break
    else:
        print(a_sorted[5][1])
