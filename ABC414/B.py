#!/usr/bin/python3

# B - String Too Long
# https://atcoder.jp/contests/abc414/tasks/abc414_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
8
m 1
i 1
s 2
i 1
s 2
i 1
p 2
i 1
<expected> mississippi

7
a 1000000000000000000
t 1000000000000000000
c 1000000000000000000
o 1000000000000000000
d 1000000000000000000
e 1000000000000000000
r 1000000000000000000
<expected> Too Long

1
a 100
<expected> aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

6
g 4
j 1
m 4
e 4
d 3
i 4
<expected> ggggjmmmmeeeedddiiii

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())

# char = []
# too_long = False
# for _ in range(N):
#     c, l = input().split()
#     if (len(char) + int(l)) > 100:
#         too_long = True
#     else:
#         char.extend([c for _ in range(int(l))])

string = ""
too_long = False
for _ in range(N):
    c, l = input().split()
    if (len(string) + int(l)) > 100:
        too_long = True
    else:
        string += c * int(l)

if too_long:
    print("Too Long")
else:
    print(string)
