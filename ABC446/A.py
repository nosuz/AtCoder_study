#!/usr/bin/python3

# A - Handmaid
# https://atcoder.jp/contests/abc446/tasks/abc446_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
Glen
<expected> Ofglen

I
<expected> Ofi

Fred
<expected> Offred

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


S = input()

print("Of" + S.lower())
