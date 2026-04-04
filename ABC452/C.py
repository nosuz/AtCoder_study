#!/usr/bin/python3

# C - Fishbones
# https://atcoder.jp/contests/abc452/tasks/abc452_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
5
5 3
5 2
4 1
5 1
3 2
8
retro
chris
itchy
tuna
crab
rock
cod
ash
<expected> Yes
Yes
No
No
No
No
No
No

5
5 1
5 2
5 3
5 4
5 5
8
retro
chris
itchy
tuna
crab
rock
cod
ash
<expected> Yes
Yes
Yes
No
No
No
No
No

"""

import os
from collections import defaultdict


# remove or comment out `debug()` before upload.
# the cost is not negligible
def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
keys = []
for i in range(N):
    A, B = map(int, input().split())
    keys.append((A, B - 1))

M = int(input())
words = []
dictionary = defaultdict(set)
for _ in range(M):
    S = input()
    words.append(S)

    for i in range(len(S)):
        dictionary[(len(S), i)].add(S[i])
debug(dictionary)

for word in words:
    debug(word)
    if len(word) != N:
        print("No")
        continue

    ans = "Yes"
    for i in range(len(word)):
        A, B = keys[i]
        debug(f"key:{word[i]},A:{A},B:{B},{dictionary[(A, B)]}")
        if not word[i] in dictionary[(A, B)]:
            ans = "No"
            break
    print(ans)
