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
for a in range(1, 7):
    for b in range(1, 7):
        if (a + b) >= x:
            comb.add(f"{a}, {b}")
        elif abs(a - b) >= y:
            comb.add(f"{a}, {b}")
# print(comb)
if len(comb) == 0:
    # this is not required if 0.0 is acceptable.
    print(0)
else:
    print(len(comb) * ((1/6) ** 2))
