#!/usr/bin/python3

# B - Change
# https://atcoder.jp/contests/abc475/tasks/abc475_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
3
1296 110 1
<expected> 13 18 24

12
3141 592 65358 9 79 323 84 6264 3 38327 950 28
<expected> 52 59 82

1
800
<expected> 0 0 2

1
980
<expected> 0 2 0

1
1000
<expected> 0 0 0

"""

import os


# remove or comment out `debug()` before upload.
# the cost is not negligible
def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
A = list(map(int, input().split()))

# 1000円札は、10^100枚。
# 買い物は10^5円までを1000回なので、1000円札が足りなくなることはない。
# よって、お釣りだけを考える。

wallet = [0, 0, 0]

for a in A:
    change = (1000 - a % 1000) % 1000  # お釣りの1000円未満の部分を考える。
    wallet[2] += change // 100
    change = change % 100
    wallet[1] += change // 10
    change = change % 10
    wallet[0] += change

print(" ".join(map(str, wallet)))
