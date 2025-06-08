#!/usr/bin/python3

# python3 validate.py sample.py

# https://atcoder.jp/contests/abc409/tasks/abc409_b

"""TEST_DATA
3
1 2 1
<expected> 1

7
1 6 2 10 2 3 2
<expected> 3

4
1 3 3 3
<expected> 3

2
100 101
<expected> 2
"""

n = int(input())
a = list(map(int, input().split()))

a.sort()

prev = -1
for i in range(len(a)):
    if a[i] == prev:
        continue

    if a[i] > (n - i):
        for x in range(a[i] - 1, prev, -1):
            if x <= (n - i):
                print(x)
                exit()
        print(prev)
        exit()

    prev = a[i]
print(a[-1])
