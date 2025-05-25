#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
9 3
<expected> 0.555555555555555555555555555555

13 6
<expected> 0

10 3
<expected> 0.5


"""

x, y = map(int, input().split())

comb = set()
for x_i in range(1, 7):
    for y_i in range(1, 7):
        if (x_i + y_i) >= x:
            comb.add(f"{x_i}, {y_i}")
        elif abs(x_i - y_i) >= y:
            comb.add(f"{x_i}, {y_i}")
            pass
# print(comb)
if len(comb) == 0:
    # this is not required if 0.0 is acceptable.
    print(0)
else:
    print(len(comb) * ((1/6) ** 2))
