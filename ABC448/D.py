#!/usr/bin/python3

# D - Integer-duplicated Path
# https://atcoder.jp/contests/abc448/tasks/abc448_d

# python ../validate.py D.py

# pytest tests/test_d.py
# pytest tests/test_d.py -k sample1

"""TEST_DATA
5
1 3 2 1 2
1 2
1 3
3 4
3 5
<expected> No
No
No
Yes
Yes

2
1000000000 1000000000
2 1
<expected> No
Yes

10
10 7 3 9 1 3 8 5 7 10
3 6
8 6
6 1
9 7
7 10
5 4
4 2
10 2
1 9
<expected> No
Yes
Yes
Yes
Yes
No
No
No
No
Yes

"""

import os
from collections import defaultdict
from collections import deque


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
A = list(map(int, input().split()))

path = defaultdict(list)
for i in range(N - 1):
    U, V = map(lambda x: int(x) - 1, input().split())
    path[U].append(V)
    path[V].append(U)
debug(path)

ans = ["No" for _ in range(N)]
visited = [False for _ in range(N)]
track = defaultdict(int)
# listは、`append()`でも $O(1)$ でない場合がある。
stack = deque()
# Tuple: node, 既にYesか, enter
stack.append((0, False, True))

# 深さ優先探索
# 木構造なので、ループはないはず。
while stack:
    node, yes, enter = stack.pop()
    # 再帰の代わりに終了マークをスタックに積む。
    if enter:
        visited[node] = True
        debug(f"n:{node}, y:{yes}")

        # 既にYesになったpathは、必ずYes
        # そうでなければ、nodeの値がこれまでのpathに含まれるか
        if yes or (track[A[node]] > 0):
            ans[node] = "Yes"
            # 一度Yesになったら、以降はYes
            yes = True
        track[A[node]] += 1

        # 戻ってきた
        stack.append((node, yes, False))

        for n in path[node]:
            if not visited[n]:
                # valuesが関係ないnodeでも共有されてしまう。
                stack.append((n, yes, True))
    else:
        track[A[node]] -= 1

print(*ans)
