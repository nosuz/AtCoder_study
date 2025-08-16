#!/usr/bin/python3

# python3 validate.py sample.py

# B - Get Min
# https://atcoder.jp/contests/abc419/tasks/abc419_b

"""TEST_DATA
5
1 6
1 7
2
1 1
2
<expected> 6 1

8
1 5
1 1
1 1
1 9
2
2
1 2
2
<expected> 1 1 2


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


Q = int(input())

x = []
for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x.append(query[1])
    elif query[0] == 2:
        debug("x:", x)
        ans = min(x)
        print(ans)
        x.remove(ans)
