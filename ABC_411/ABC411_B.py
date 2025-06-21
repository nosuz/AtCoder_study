#!/usr/bin/python3

# python3 validate.py sample.py

# B - Distance Table
# https://atcoder.jp/contests/abc411/tasks/abc411_b

"""TEST_DATA
5
5 10 2 3
<expected> 5 15 17 20 10 12 15 2 5 3

2
100
<expected> 100


"""

n = int(input())
d = list(map(int, input().split()))

for i in range(n):
    dist = 0
    result = []
    for j in d[i:]:
        dist += j
        result.append(dist)
    print(*result)
