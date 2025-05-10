#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
2000 1
<expected> Yes

1000 1
<expected> No

1500 2
<expected> Yes

2800 2
<expected> No


"""

r, x = map(int, input().split())

# print(f"x: {x}, r: {r}")
if x == 1:
    if 1600 <= r <= 2999:
        print("Yes")
    else:
        print("No")

elif x == 2:
    if 1200 <= r <= 2399:
        print("Yes")
    else:
        print("No")

else:
    print("No")
