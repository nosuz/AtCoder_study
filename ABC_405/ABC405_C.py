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

# sum = 0
# for i in range(n - 1, 0, -1):
#     sum += a[i]
#     total += a[i-1] * sum

# sum = sum(a)
# for i in range(0, n - 1):
#     sum -= a[i]
#     total += a[i] * sum
# print(total)

# [@ila_o_](https://x.com/ila_o_/status/1921204887305564572)
sum = sum(a) ** 2
for i in range(0, n - 1):
    sum -= a[i]**2
print(sum / 2)
