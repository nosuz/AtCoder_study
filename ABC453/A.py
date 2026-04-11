#!/usr/bin/python3

# A - Trimo
# https://atcoder.jp/contests/abc453/tasks/abc453_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
7
ooparts
<expected> parts

6
abcooo
<expected> abcooo

5
ooooo
<expected>

"""

import os
import re


# remove or comment out `debug()` before upload.
# the cost is not negligible
def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
S = input()

print(re.sub(r"^o*", "", S))
