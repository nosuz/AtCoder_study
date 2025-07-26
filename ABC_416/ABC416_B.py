#!/usr/bin/python3

# python3 validate.py sample.py

# B - 1D Akari
# https://atcoder.jp/contests/abc416/tasks/abc416_b

"""TEST_DATA
#..#.
<expected> #o.#o

#
<expected> #

.....
<expected> ..o..

...#..#.##.#.
<expected> o..#.o#o##o#o


"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


S = input()

s = S.split("#")
debug(s)

T = []
for i in s:
    if i == '':
        T.append('')
    else:
        T.append('o' + '.' * (len(i) - 1))
print("#".join(T))
