#!/usr/bin/python3

# python3 validate.py sample.py

# A - AtCoder Language
# https://atcoder.jp/contests/abc419/tasks/abc419_a

"""TEST_DATA
red
<expected> SSS

atcoder
<expected> Unknown


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


S = input()

if S == "red":
    print("SSS")
elif S == "blue":
    print("FFF")
elif S == "green":
    print("MMM")
else:
    print("Unknown")
