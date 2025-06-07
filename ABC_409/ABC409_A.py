#!/usr/bin/python3

# python3 validate.py sample.py

# https://atcoder.jp/contests/abc409/tasks/abc409_a

"""TEST_DATA
4
oxoo
xoox
<expected> Yes

5
xxxxx
ooooo
<expected> No

10
xoooxoxxxo
ooxooooxoo
<expected> Yes


"""

n = int(input())

t = list(input())
a = list(input())

for x, y in zip(t, a):
    if (x == 'o') and (y == 'o'):
        print("Yes")
        exit()
print("No")
