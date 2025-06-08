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

1
0
<expected> 0

2
0 1
<expected> 1

"""

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(lambda: 0)
for i in range(len(a)):
    d[a[i]] += 1
# print(d)

for x in range(101):
    count = 0
    for k, v in d.items():
        if k >= x:
            count += v
    # print(x, count)
    if count < x:
        # 条件を満たさない。一つ前は満たしていたはず。
        print(x-1)
        exit()
# LTE debug
# while True:
#     continue

# x = 100でも条件を満たしている
print(100)
