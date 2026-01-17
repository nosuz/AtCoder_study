#!/usr/bin/python3

# B - Two Languages
# https://atcoder.jp/contests/abc441/tasks/abc441_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
6 5
ahikst
aikot
5
asahi
okita
kiai
hash
it
<expected> Takahashi
Aoki
Unknown
Takahashi
Unknown

7 6
ahiknst
ahikos
5
kioki
ohiki
tashi
nishi
kashi
<expected> Aoki
Aoki
Takahashi
Takahashi
Unknown

13 11
defghiqsvwxyz
acejmoqrtwx
15
qhsqzhd
jcareec
wwqxqew
wxqxwex
jxxrtwa
trtqjxe
sqyggse
xxqwxew
xewwxxw
wwqxwex
xqqxqwq
qxxexxe
teqeroc
eeeqqee
vxdevyy
<expected> Takahashi
Aoki
Unknown
Unknown
Aoki
Aoki
Takahashi
Unknown
Unknown
Unknown
Unknown
Unknown
Aoki
Unknown
Takahashi

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, M = map(int, input().split())

S = input()
T = input()
Q = int(input())

s_char = set(list(S))
t_char = set(list(T))
com_char = t_char.intersection(s_char)

debug(t_char)
debug(s_char)
debug(com_char)

for q in range(Q):
    w = set(list(input()))
    for c in w:
        if not c in com_char:
            if c in s_char:
                print("Takahashi")
                break
            if c in t_char:
                print("Aoki")
                break
    else:
        print("Unknown")
