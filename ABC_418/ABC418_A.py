#!/usr/bin/python3

# python3 validate.py sample.py

# A - I'm a teapot
# https://atcoder.jp/contests/abc418/tasks/abc418_a

"""TEST_DATA
8
greentea
<expected> Yes

6
coffee
<expected> No

3
tea
<expected> Yes

1
t
<expected> No


"""

import re
import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
S = input()

if re.search(r'tea$', S):
    print("Yes")
else:
    print("No")
