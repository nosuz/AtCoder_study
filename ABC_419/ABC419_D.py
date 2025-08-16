#!/usr/bin/python3

# python3 validate.py sample.py

# D - Substr Swap
# https://atcoder.jp/contests/abc419/tasks/abc419_d

"""TEST_DATA
5 3
apple
lemon
2 4
1 5
5 5
<expected> lpple

10 5
lemwrbogje
omsjbfggme
5 8
4 8
1 3
6 6
1 4
<expected> lemwrfogje


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, M = map(int, input().split())
S = input()
T = input()

selector = [0] * (N+1)
for _ in range(M):
    L, R = map(int, input().split())
    selector[L - 1] += 1
    selector[R] -= 1
debug("selector:", selector)

index = 0
ans = []
for i in range(N):
    index += selector[i]
    if index % 2 == 0:
        ans.append(S[i])
    else:
        ans.append(T[i])
print("".join(ans))
