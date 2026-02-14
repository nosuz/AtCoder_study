#!/usr/bin/python3

# A - Strong Word
# https://atcoder.jp/contests/abc445/tasks/abc445_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
luminol
<expected> Yes

rule
<expected> No

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


S = input()

if S[0] == S[-1]:
    print("Yes")
else:
    print("No")
