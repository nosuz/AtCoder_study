#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
5 2
7 13 3 2 5
<expected> 10

2 1
2 5
<expected> 1


"""

import math

n, k = map(int, input().split())

a = list(map(int, input().split()))

display = 1

for i in a:
    display *= i
    # print(display)

    # why log10 not work?
    # print(math.log10(display))
    # if math.log10(display) >= k:
    #     display = 1

    if display > 10 ** k - 1:
        display = 1
print(display)
