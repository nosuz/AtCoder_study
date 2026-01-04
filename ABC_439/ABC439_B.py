#!/usr/bin/python3

# python3 validate.py sample.py

# B - Happy Number
# https://atcoder.jp/contests/abc439/tasks/abc439_b

"""TEST_DATA
2026
<expected> Yes

439
<expected> No

440
<expected> Yes

1
<expected> Yes

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = list(input())

if len(N) == 1:
    n = int(N[0])
    total = n*n
    if total == 1:
        print("Yes")
    else:
        print("No")
else:
    while len(N) > 1:
        total = 0
        for x in N:
            n = int(x)
            total += n*n
        if total == 1:
            break

        N = list(str(total))
    else:
        print("No")
        exit()
    print("Yes")
