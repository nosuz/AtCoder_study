#!/usr/bin/python3

# python3 validate.py sample.py

# B - Precondition
# https://atcoder.jp/contests/abc412/tasks/abc412_b

"""TEST_DATA
AtCoder
Total
<expected> Yes

aBCdE
abcdcba
<expected> No

abcde
XYZ
<expected> Yes


"""

s = input()
t = input()

upper_char = 0
contain_char = 0
for i in range(1, len(s)):
    x = s[i]
    if x.isupper():
        upper_char += 1
        y = s[i - 1]
        if y in t:
            contain_char += 1

if upper_char == contain_char:
    print("Yes")
else:
    print("No")
