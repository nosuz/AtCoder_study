#!/usr/bin/python3

# B - Split Ticketing
# https://atcoder.jp/contests/abc450/tasks/abc450_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
3
45 450
45
<expected> Yes

4
25 40 65
30 55
25
<expected> No

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())

costs = []
for _ in range(N-1):
    C = list(map(int, input().split()))
    costs.append(C)

debug(costs)
for a in range(N-2):
    for b in range(a+1, N-1):
        for c in range(b+1, N):
            # 一旦改札の外に出たほうが安い時に`Yes`
            debug(f"AC:{costs[a][c-a-1]} > (AB:{costs[a][b-a-1]} + BC:{costs[b][c-b-1]})")
            if costs[a][c-a-1] > (costs[a][b-a-1] + costs[b][c-b-1]):
                print("Yes")
                break
        else:
            continue
        break
    else:
        continue
    break
else:
    print("No")
