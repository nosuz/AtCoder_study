#!/usr/bin/python3

# python3 validate.py sample.py

# A - G1
# https://atcoder.jp/contests/abc410/tasks/abc410_a

"""TEST_DATA
5
3 1 4 1 5
4
<expected> 2

1
1
100
<expected> 0

15
18 89 31 2 15 93 64 78 58 19 79 59 24 50 30
38
<expected> 8


"""

n = int(input())
a = list(map(int, input().split()))
k = int(input())

# count = 0

# for i in a:
#     if i >= k:
#         count += 1
# print(count)

entry = [True if i >= k else False for i in a]
print(sum(entry))
