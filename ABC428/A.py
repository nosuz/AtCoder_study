#!/usr/bin/python3

# A - Grandma's Footsteps
# https://atcoder.jp/contests/abc428/tasks/abc428_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
7 3 2 11
<expected> 49

6 3 2 9
<expected> 36

1 1 666 428
<expected> 1

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)

S, A, B, X = map(int, input().split())

run_time = (X // (A+B)) * A # 走れるのは、A期間だけ。
time_mod = X % (A+B)
if time_mod < A:
    run_time += time_mod
else:
    run_time += A
print(run_time*S)
