#!/usr/bin/python3

# python3 validate.py sample.py

# B - Most Minority
# https://atcoder.jp/contests/abc420/tasks/abc420_b

"""TEST_DATA
3 5
11100
10101
01110
<expected> 2 3

5 4
0000
0000
0000
0000
0000
<expected> 1 2 3 4 5

7 8
11010011
01000000
01111100
10111000
10011110
10100101
10010110
<expected> 1 2 3


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, M = map(int, input().split())

p = [0] * N
vote = []
for _ in range(N):
    S = list(input())
    # debug(S)
    vote.append(S)
debug(vote)

for col in range(M):
    count_0 = 0
    count_1 = 0
    for row in range(N):
        debug(f"{col},{row}")
        if vote[row][col] == '0':
            count_0 += 1
        else:
            count_1 += 1

    if (count_0 == 0) or (count_1 == 0):
        for i in range(N):
            p[i] += 1
    elif count_0 < count_1:
        debug("Point to 0")
        for row in range(N):
            if vote[row][col] == '0':
                p[row] += 1
    else:
        debug("Point to 1")
        for row in range(N):
            if vote[row][col] == '1':
                p[row] += 1

max_point = max(p)
debug(f"max: {max_point}")
ans = []
for i in range(N):
    if p[i] == max_point:
        ans.append(i + 1)
print(*ans)
