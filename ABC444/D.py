#!/usr/bin/python3

# D - Many Repunit Sum
# https://atcoder.jp/contests/abc444/tasks/abc444_d

# python ../validate.py D.py

# pytest tests/test_d.py
# pytest tests/test_d.py -k sample1

"""TEST_DATA
4
3 3 3 3
<expected> 444

3
30 10 20
<expected> 111111111122222222223333333333

10
1 2 3 4 5 6 7 8 9 10
<expected> 1234567900

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
A = list(map(int, input().split()))

imos = [0] * (max(A) + 1)
for a in A:
    imos[a] += 1
# print(imos)

total = []
carrier = 0
for i in range(len(imos)):
    if imos[i] > 0:
        N -= imos[i]
    sum = N + carrier  # N = 1 * N
    digit = sum % 10
    total.append(digit)
    carrier = sum // 10
total.append(carrier)
# print(total)
str = []
header = True
last_index = len(total) - 1
for i in range(len(total)):
    if header:
        # trim leading 0
        if total[last_index - i] != 0:
            print(total[last_index - i], end="")
            header = False
    else:
        print(total[last_index - i], end="")
print()
