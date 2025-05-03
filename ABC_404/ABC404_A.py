#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
a
<expected> d

abcdfhijklmnopqrstuvwxyz
<expected> e

qazplwsxokmedcijnrfvuhbgt
<expected> y


"""

s = input()

char = set([s[i] for i in range(len(s))])
# print(char)

for i in range(26):
    if not chr(0x61 + i) in char:
        print(chr(0x61 + i))
        exit()
