#!/usr/bin/python3

# C - Sneaking Glances
# https://atcoder.jp/contests/abc453/tasks/abc453_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
5
2 5 2 2 1
<expected> 4

5
100 1 2 3 4
<expected> 1

20
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
<expected> 20

"""

import os


# remove or comment out `debug()` before upload.
# the cost is not negligible
def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


def fliped(a, b):
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return False
    else:
        return True


def move(count, p, pos):
    if p == len(L):
        return count

    # right
    next_pos = pos + L[p]
    if fliped(pos, next_pos):
        next_count = count + 1
    else:
        next_count = count
    count_right = move(next_count, p + 1, next_pos)

    # left
    next_pos = pos - L[p]
    if fliped(pos, next_pos):
        next_count = count + 1
    else:
        next_count = count
    count_left = move(next_count, p + 1, next_pos)

    return max(count_left, count_right)


N = int(input())
L = list(map(int, input().split()))
L = [l * 2 for l in L]

right = False
count = move(0, 0, 1)
print(count)
