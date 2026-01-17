#!/usr/bin/python3

# D - Paid Walk
# https://atcoder.jp/contests/abc441/tasks/abc441_d

# python ../validate.py D.py

# pytest tests/test_d.py
# pytest tests/test_d.py -k sample1

"""TEST_DATA
5 8 3 80 100
1 2 20
1 3 70
2 1 30
2 5 10
3 2 10
3 4 30
3 5 20
5 1 70
<expected> 1 5

10 1 1 1 100
2 3 1
<expected>

2 5 3 1 100
1 1 1
2 2 100
1 2 1
1 2 1
1 2 100
<expected> 1 2

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, M, L, S, T = map(int, input().split())


path = [[] for i in range(N+1)]
for n in range(M):
    U, V, C = map(int, input().split())
    path[U].append((V, C))

debug(path)
debug(path[0])

reached = set()


def walk(node, cost, step):
    if step == L:
        if S <= cost <= T:
            reached.add(node)
    else:
        for p in path[node]:
            walk(p[0], cost + p[1], step + 1)


for p in path[1]:
    walk(p[0], p[1], 1)

if len(reached) == 0:
    print("")
else:
    print(*sorted(reached))
