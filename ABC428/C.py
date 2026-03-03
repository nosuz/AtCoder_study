#!/usr/bin/python3

# C - Brackets Stack Query
# https://atcoder.jp/contests/abc428/tasks/abc428_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
8
1 (
2
1 (
1 )
2
1 (
1 )
1 )
<expected> No
Yes
No
Yes
No
No
No
Yes

4
1 )
1 (
1 )
1 (
<expected> No
No
No
No


"""

import os

def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())

blacket_sum = [0] * (N+1)
blacket_phase = [0] * (N+1)
p = 0
for _ in range(N):
    query = input().split()

    p += 1
    if query[0] == "1":
        if query[1] == "(":
            blacket_sum[p] = blacket_sum[p-1] + 1
            if blacket_phase[p-1] >= 0:
                blacket_phase[p] = blacket_phase[p-1] + 1
            else:
                blacket_phase[p] = 1
        else:
            blacket_sum[p] = blacket_sum[p-1] - 1
            blacket_phase[p] = blacket_phase[p-1] - 1
    else:
        p -= 2
        if p < 0:
            p = 0

    debug(p)
    debug(blacket_sum)
    debug(blacket_phase)
    if (blacket_sum[p] == 0) and (blacket_phase[p] == 0):
        print("Yes")
    else:
        print("No")
