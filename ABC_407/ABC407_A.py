#!/usr/bin/python3

# python3 validate.py sample.py

# A - Approximation
# https://atcoder.jp/contests/abc407/tasks/abc407_a

"""TEST_DATA
4 7
<expected> 1

407 29
<expected> 14

22 11
<expected> 2


"""

# import math

a, b = map(int, input().split())

# print(math.floor(a / b + 0.5))
# expected to fail, but round() worked.
print(round(a / b))
