#!/usr/bin/python3

# D - Reachability Query 2
# https://atcoder.jp/contests/abc435/tasks/abc435_d

# python ../validate.py D.py

# pytest tests/test_d.py
# pytest tests/test_d.py -k sample1

"""TEST_DATA
5 6
1 2
2 3
3 1
4 5
1 4
2 5
5
1 3
2 1
2 4
1 5
2 4
<expected> Yes
No
Yes

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


# def BFS(path, n):
#     visited = set()
#     visited.add(n)

#     que = list(path[n])
#     while (len(que) > 0):
#         i = que.pop()
#         if not i in visited:
#             visited.add(i)
#             que += list(path[i])
#     return visited


N, M = map(int, input().split())
# 素直な有向グラフを作るのではなく、
# 逆にたどるために逆向き有向グラフを作る。
reverse_path = [set() for _ in range(N+1)]
for m in range(M):
    X, Y = map(int, input().split())
    reverse_path[Y].add(X)
debug(reverse_path)

# visited nodes 情報をBFS間で共有するイメージ
reachable = set()

debug("--")
black = set()
Q = int(input())
for _q in range(Q):
    C, V = map(int, input().split())
    match C:
        case 1:
            # V に到達可能な頂点を共有BFSで探索
            if not V in reachable:
                # スタート頂点を入れるのを忘れない。
                reachable.add(V)

                que = list(reverse_path[V])
                while (len(que) > 0):
                    i = que.pop()
                    if not i in reachable:
                        reachable.add(i)
                        que += list(reverse_path[i])
        case 2:
            if V in reachable:
                print("Yes")
            else:
                print("No")
