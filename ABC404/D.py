#!/usr/bin/python3

# D - Goin' to the Zoo
# https://atcoder.jp/contests/abc404/tasks/abc404_d

# python ../validate.py D.py

# pytest tests/test_d.py
# pytest tests/test_d.py -k sample1

"""TEST_DATA
4 3
1000 300 700 200
3 1 3 4
3 1 2 4
2 1 3
<expected> 1800

7 6
500 500 500 500 500 500 1000
3 1 2 7
3 2 3 7
3 3 4 7
3 4 5 7
3 5 6 7
3 6 1 7
<expected> 2000

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


def visit(place, paid):
    if place == N:
        # 全ての動物園を0-2回訪問した。
        two_times = [True for c in watched if c >= 2]
        if len(two_times) == M:
            # 全ての動物を２回以上見た。
            total_cost.append(paid)
        return

    # 同じ動物園を訪問する回数は、最大でも2回。
    for c in [0, 1, 2]:
        for a in zoo[place]:
            watched[a] += c
        paid += C[place] * c
        visit(place + 1, paid)

        for a in zoo[place]:
            watched[a] -= c
        paid -= C[place] * c


N, M = map(int, input().split())
C = list(map(int, input().split()))

# 動物園毎に飼育している動物のリストを作成する。
zoo = [[] for _ in range(N)]
for animal in range(M):
    A = list(map(lambda x: int(x) - 1, input().split()))
    for z in A[1:]:
        zoo[z].append(animal)
debug(zoo)

watched = [0 for _ in range(M)]
total_cost = []
visit(0, 0)
print(min(total_cost))
