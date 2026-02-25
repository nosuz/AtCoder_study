#!/usr/bin/python3

# A - Sigma Cubes
# https://atcoder.jp/contests/abc425/tasks/abc425_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
3
<expected> -20

9
<expected> -425

10
<expected> 575

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())

ans = 0

for n in range(1, N+1):
    if (n%2) == 1:
        ans += -(n ** 3)
    else:
        ans += n ** 3
print(ans)
