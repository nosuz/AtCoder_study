#!/usr/bin/python3

# A - π
# https://atcoder.jp/contests/abc449/tasks/abc449_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
2
<expected> 3.141592653589793

7
<expected> 38.48451000647496

98
<expected> 7542.9639612690935

"""

import os
import math


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


D = int(input())

r = D / 2.0
print(math.pi * r * r)
