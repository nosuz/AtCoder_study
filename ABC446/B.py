#!/usr/bin/python3

# B - Greedy Draft
# https://atcoder.jp/contests/abc446/tasks/abc446_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
4 5
3
3 1 2
3
3 2 1
2
2 3
4
2 5 3 1
<expected> 3
2
0
5

6 5
1
3
2
3 5
5
5 3 1 4 2
5
5 1 3 4 2
5
3 4 1 5 2
5
5 1 3 2 4
<expected> 3
5
1
4
2
0

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, M = map(int, input().split())
drinks = [True for _ in range(M)]  # True: available
for _ in range(N):
    L = int(input())  # 不要
    # 希望リスト
    X = list(map(lambda x: int(x) - 1, input().split()))
    for x in X:
        if drinks[x]:
            print(x+1)
            drinks[x] = False
            break
    else:
        print(0)
