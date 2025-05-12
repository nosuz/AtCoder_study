#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
5 3
3 2 3 1 2
<expected> 2

4 3
1 3 1 3
<expected> 0

10 4
1 3 3 4 2 1 3 1 2 4
<expected> 6


"""

n, m = map(int, input().split())

a = list(map(int, input().split()))

expected = set([i for i in range(1, m + 1)])
# print(expected)
for i in range(n):
    if a[i] in expected:
        expected.remove(a[i])
        if len(expected) == 0:
            print(n - i)
            exit()
print(0)

# expected = [False for _ in range(m)]
# # print(expected)
# for i in range(n):
#     tmp = a[i]
#     if tmp <= m:
#         expected[tmp - 1] = True
#         if all(expected):
#             print(n - i)
#             exit()
# print(0)
