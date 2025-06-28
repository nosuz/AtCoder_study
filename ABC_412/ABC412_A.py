#!/usr/bin/python3

# python3 validate.py sample.py

# A - Task Failed Successfully
# https://atcoder.jp/contests/abc412/tasks/abc412_a

"""TEST_DATA
4
2 8
5 5
5 4
6 7
<expected> 2

5
1 1
1 1
1 1
1 1
1 1
<expected> 0

6
1 6
2 5
3 4
4 3
5 2
6 1
<expected> 3


"""

n = int(input())

ok = 0
for _ in range(n):
    a, b = map(int, input().split())

    if a < b:
        ok += 1
print(ok)
