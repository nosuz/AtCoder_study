#!/usr/bin/python3

# A - Seats 2
# https://atcoder.jp/contests/abc447/tasks/abc447_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
6 3
<expected> Yes

4 3
<expected> No

5 3
<expected> Yes

44 7
<expected> Yes

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)

N, M = map(int, input().split())

max_person = (N+1) // 2
if max_person >= M:
    print("Yes")
else:
    print("No")
