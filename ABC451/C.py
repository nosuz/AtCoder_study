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
import heapq


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


Q = int(input())

trees = []
for _ in range(Q):
    command, height = map(int, input().split())
    if command == 1:
        # 植える
        heapq.heappush(trees, height)
    else:
        # 切る
        while len(trees):
            if trees[0] > height:
                break
            heapq.heappop(trees)
    debug(trees)
    print(len(trees))
