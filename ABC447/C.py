#!/usr/bin/python3

# C - Insert and Erase A
# https://atcoder.jp/contests/abc447/tasks/abc447_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
ABC
BACA
<expected> 3

ABC
ARC
<expected> -1

ABC
ABC
<expected> 0

AAAWAZAAAABAAAU
AWAAZABAAAAAUA
<expected> 9

"""

import os

def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)

S = input()
S = S + "|" # 最後にガードを入れる
T = input()
T = T + "|"

S_a = S.replace("A", "")
T_a = T.replace("A", "")

if S_a != T_a:
    print(-1)
else:
    steps = 0
    i = 0
    j = 0
    while (i < len(S)) and (j < len(T)):
        debug(i,j)
        i_begin = i
        while S[i] == "A":
            i += 1
        j_begin = j
        while T[j] == "A":
            j += 1

        i_delta = i - i_begin
        j_delta = j - j_begin
        steps += abs(i_delta - j_delta)
        i += 1
        j += 1
    print(steps)
