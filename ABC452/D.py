#!/usr/bin/python3

# D - No-Subsequence Substring
# https://atcoder.jp/contests/abc452/tasks/abc452_d

# python ../validate.py D.py

# pytest tests/test_d.py
# pytest tests/test_d.py -k sample1

"""TEST_DATA
abrakadabra
aba
<expected> 51

aaaaa
a
<expected> 0

rdddrdtdcdrrdcredctdordoeecrotet
dcre
<expected> 263

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


S = input()
T = input()

start = 0
end = 0
ans = 0
pointer = [0 for _ in range(len(T))]
while start < len(S):
    j = 0
    for i in range(start, len(S)):
        if S[i] == T[j]:
            pointer[j] = i
            if j == (len(T) - 1):
                # T を含むのを見つけた。
                debug(pointer)
                ans += pointer[-1] - start
                break
            elif pointer[j] >= pointer[j + 1]:
                j += 1
            else:
                debug(pointer)
                ans += pointer[-1] - start
                break
    else:
        debug(f"no match:{start}")
        # debug(f"ans:{ans}")
        delta = len(S) - start
        ans += (1 + delta) * delta // 2
        break
    start += 1
print(ans)
