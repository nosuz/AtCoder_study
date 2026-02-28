#!/usr/bin/python3

# D - Take ABC 2
# https://atcoder.jp/contests/abc447/tasks/abc447_d

# python ../validate.py D.py

# pytest tests/test_d.py
# pytest tests/test_d.py -k sample1

"""TEST_DATA
ABACBCC
<expected> 2

CBACBB
<expected> 0

BBBAAABCBCBAACBBCAAC
<expected> 5

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)

S = input()

count = 0
i = 0
j = 0
k = 0
while (i < len(S)) and (j < len(S)) and (k < len(S)):
    # find A
    while (i < len(S)) and (S[i] != "A"):
        i += 1

    # find B
    j = max(j, i + 1)
    while (j < len(S)) and (S[j] != "B"):
        j += 1

    # find C
    k = max(k, j + 1)
    while (k < len(S)) and (S[k] != "C"):
        k += 1

    if (i < len(S)) and (j < len(S)) and (k < len(S)):
        count += 1

    # next
    i += 1
    j += 1
    k += 1
print(count)
