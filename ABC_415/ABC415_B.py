#!/usr/bin/python3

# python3 validate.py sample.py

# B - Pick Two
# https://atcoder.jp/contests/abc415/tasks/abc415_b

"""TEST_DATA
.#.##..##.#.###....#
<expected> 2,4 5,8 9,11 13,14 15,20


"""

S = input()

location = []
for i in range(len(S)):
    if S[i] == "#":
        location.append(i+1)

for i in range(0, len(location), 2):
    print(f"{location[i]},{location[i+1]}")
