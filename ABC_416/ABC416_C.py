#!/usr/bin/python3

# python3 validate.py sample.py

# C - Concat (X-th)
# https://atcoder.jp/contests/abc416/tasks/abc416_c

"""TEST_DATA
3 2 6
abc
xxx
abc
<expected> abcxxx

5 5 416
a
aa
aaa
aa
a
<expected> aaaaaaa


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N, K, X = map(int, input().split())

S = []
for _ in range(N):
    S.append(input())

words = S
cat = 1
while cat < K:
    next_words = []
    for w in words:
        for ww in S:
            next_words.append(w + ww)
    cat += 1
    words = next_words
words.sort()
print(words[X-1])
