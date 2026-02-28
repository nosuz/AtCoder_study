#!/usr/bin/python3

# B - mpp
# https://atcoder.jp/contests/abc447/tasks/abc447_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
mississippi
<expected> mpp

atcoder
<expected>

beginner
<expected> bgir

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)

S = input()

count = dict()
max_count = 0
for i in range(len(S)):
    c = S[i]
    if not c in count:
        count[c] = 1
    else:
        count[c] += 1
    if max_count < count[c]:
        max_count = count[c]

for i in range(len(S)):
    c = S[i]
    if count[c] != max_count:
        print(c, end="")
print()
