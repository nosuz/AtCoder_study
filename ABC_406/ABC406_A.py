#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
22 40 22 30
<expected> Yes

22 40 22 45
<expected> No

12 0 11 30
<expected> Yes


"""

a, b, c, d = map(int, input().split())

if c < a:
    print("Yes")
elif (c == a) and (d < b):
    print("Yes")
else:
    print("No")
