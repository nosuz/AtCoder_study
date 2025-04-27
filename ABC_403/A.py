#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
7
3 1 4 1 5 9 2
<expected> 14

1
100
<expected> 100

14
100 10 1 10 100 10 1 10 100 10 1 10 100 10
<expected> 403
"""

n = int(input())
a = list(map(int, input().split()))

sum = 0
for i in range(0, n, 2):
    sum += a[i]

print(sum)
