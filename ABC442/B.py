#!/usr/bin/python3

# B - Music Player
# https://atcoder.jp/contests/abc442/tasks/abc442_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
10
2
1
3
1
3
1
1
3
2
2
<expected> No
No
No
No
No
No
No
Yes
Yes
No

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


Q = int(input())

volume = 0
play = False
for i in range(Q):
    A = int(input())

    match A:
        case 1:
            volume += 1
        case 2:
            volume -= 1
            if volume < 0:
                volume = 0
        case 3:
            play = not play

    if play and (volume >= 3):
        print("Yes")
    else:
        print("No")
