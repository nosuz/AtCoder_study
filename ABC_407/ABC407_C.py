#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
21
<expected> 4

407
<expected> 17

2025524202552420255242025524
<expected> 150


"""

s = list(map(int, list(input())))
# print(s)

num_a = len(s)

num_b = 0
for i in range(num_a - 1, -1, -1):
    n = s[i]
    num_b += n

    s[i - 1] = (10 + s[i - 1] - num_b % 10) % 10
print(num_a + num_b)
