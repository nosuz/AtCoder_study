#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
3
4 2 3
<expected> 26

2
9 45
<expected> 405

10
7781 8803 8630 9065 8831 9182 8593 7660 7548 8617
<expected> 3227530139


"""

n = int(input())

a = list(map(int, input().split()))

total = 0
# for i in range(n - 1):
#     total += a[i] * sum(a[i + 1:])
# print(total)

sum = 0
for i in range(n - 1, 0, -1):
    sum += a[i]
    total += a[i-1] * sum
print(total)
