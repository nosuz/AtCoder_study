#!/usr/bin/python3

# A - Too Many Requests
# https://atcoder.jp/contests/abc429/tasks/abc429_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
5 3
<expected> OK
OK
OK
Too Many Requests
Too Many Requests

3 5
<expected> OK
OK
OK

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)

N, M = map(int, input().split())

for i in range(1, N+1):
    if i <= M:
        print("OK")
    else:
        print("Too Many Requests")
