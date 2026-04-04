#!/usr/bin/python3

# C - Cycle Graph?
# https://atcoder.jp/contests/abc404/tasks/abc404_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
4 4
2 4
3 1
4 1
2 3
<expected> Yes

4 6
1 2
1 3
1 4
2 3
2 4
3 4
<expected> No

"""

import os
from collections import defaultdict


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, M = map(int, input().split())

path = defaultdict(list)
for _ in range(M):
    A, B = map(lambda x: int(x) - 1, input().split())
    path[A].append(B)
    path[B].append(A)
debug(path)

stack = [0]
visited = [False] * N
while stack:
    node = stack.pop()
    visited[node] = True
    next_node = path[node]
    if len(next_node) != 2:
        # サイクルグラフには、分岐や行き止まりは無い
        break
    for n in next_node:
        if not visited[n]:
            stack.append(n)

debug(visited)
debug(sum(visited))
if sum(visited) == N:
    # 全てのnodeを回った。
    print("Yes")
else:
    print("No")
