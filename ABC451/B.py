#!/usr/bin/python3

# B - Personnel Change
# https://atcoder.jp/contests/abc451/tasks/abc451_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
5 4
1 2
2 1
3 1
2 2
2 4
<expected> 1
-1
-1
1

10 5
3 2
3 4
1 2
2 2
4 4
3 1
3 4
4 2
3 3
3 2
<expected> 0
4
-5
1
0

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, M = map(int, input().split())

pre = [0 for _ in range(M)]
post = [0 for _ in range(M)]
for _ in range(N):
    A, B = map(lambda x: int(x) - 1, input().split())
    pre[A] += 1
    post[B] += 1

# for i in range(M):
#     print(post[i] - pre[i])
for a, b in zip(pre, post):
    print(b - a)
