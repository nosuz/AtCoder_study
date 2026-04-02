#!/usr/bin/python3

# A - Not Found
# https://atcoder.jp/contests/abc404/tasks/abc404_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
a
<expected> d

abcdfhijklmnopqrstuvwxyz
<expected> e

qazplwsxokmedcijnrfvuhbgt
<expected> y

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


# s = input()

# char = set([s[i] for i in range(len(s))])
# # print(char)

# for i in range(26):
#     if not chr(0x61 + i) in char:
#         print(chr(0x61 + i))
#         exit()

chars = [chr(i) for i in range(ord("a"), ord("z") + 1)]
debug(chars)

chars_set = set(chars)

S = input()
S_set = set(list(S))

delta = chars_set - S_set
# `len(S) <= 25` なので、必ず1文字は残る。
print(delta.pop())
