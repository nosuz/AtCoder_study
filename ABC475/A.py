#!/usr/bin/python3

# A - mnclr
# https://atcoder.jp/contests/abc475/tasks/abc475_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
mtr
<expected> motor

mnclr
<expected> monocolor

oo
<expected> ooo

"""

import os


# remove or comment out `debug()` before upload.
# the cost is not negligible
def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


S = list(input())
# debug(S)

answer = []
for i in range(len(S) - 1):
    answer.append(S[i])
    answer.append("o")
answer.append(S[-1])
print("".join(answer))
