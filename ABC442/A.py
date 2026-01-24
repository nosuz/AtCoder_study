#!/usr/bin/python3

# A - Count .
# https://atcoder.jp/contests/abc442/tasks/abc442_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
aiiaj
<expected> 3

abcedfgh
<expected> 0

jjjjjj
<expected> 6

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


S = list(input())

# count = 0
# for c in S:
#     if c in ["i", "j"]:
#         count += 1

# print(count)

result = [c in ["i", "j"] for c in S]
print(sum(result))
