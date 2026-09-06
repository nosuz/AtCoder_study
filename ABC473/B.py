#!/usr/bin/python3

# B - Old Maid
# https://atcoder.jp/contests/abc473/tasks/abc473_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
8
2 7 1 8 2 8 1 8
<expected> 15

5
1 2 3 4 5
<expected> 15

15
58 97 74 16 97 74 97 16 51 52 58 52 74 32 43
<expected> 297

"""

import os


# remove or comment out `debug()` before upload.
# the cost is not negligible
def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())

A = list(map(int, input().split()))

cards = dict()

for a in A:
    if a in cards:
        cards[a] += 1
    else:
        cards[a] = 1

answer = 0
for key in cards:
    answer += (cards[key] % 2) * key
print(answer)
