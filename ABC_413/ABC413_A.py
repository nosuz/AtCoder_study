#!/usr/bin/python3

# python3 validate.py sample.py

# A - Content Too Large
# https://atcoder.jp/contests/abc413/tasks/abc413_a

"""TEST_DATA
5 15
3 1 4 1 5
<expected> Yes

5 5
3 1 4 1 5
<expected> No

1 10000
100
<expected> Yes


"""

n, m = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) <= m:
    print("Yes")
else:
    print("No")
