#!/usr/bin/python3

# python3 validate.py sample.py

# A - Required Length
# https://atcoder.jp/contests/abc411/tasks/abc411_a

"""TEST_DATA
chokudai
5
<expected> Yes

ac
3
<expected> No

atcoder
7
<expected> Yes


"""

p = input()
l = int(input())

if len(p) >= l:
    print("Yes")
else:
    print("No")
