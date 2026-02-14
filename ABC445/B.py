#!/usr/bin/python3

# B - Center Alignment
# https://atcoder.jp/contests/abc445/tasks/abc445_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
4
apple
blueberry
coconut
dragonfruit
<expected> ...apple...
.blueberry.
..coconut..
dragonfruit

6
abc
d
efghi
jkl
mnopq
r
<expected> .abc.
..d..
efghi
.jkl.
mnopq
..r..

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())

S = []
for n in range(N):
    S.append(input())
m = max([len(s) for s in S])
debug(m)

for s in S:
    x = (m - len(s)) // 2
    print("." * x + s + "." * x)
