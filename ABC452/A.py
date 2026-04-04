#!/usr/bin/python3

# A - Gothec
# https://atcoder.jp/contests/abc452/tasks/abc452_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
3 3
<expected> Yes

1 1
<expected> No

4 4
<expected> No

11 7
<expected> No

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


M, D = map(int, input().split())

if M == 1 and D == 7:
    print("Yes")
elif M == D == 3:
    print("Yes")
elif M == D == 5:
    print("Yes")
elif M == D == 7:
    print("Yes")
elif M == D == 9:
    print("Yes")
else:
    print("No")
