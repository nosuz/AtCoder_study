#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
5 10
6 11 21 22 30
<expected> Yes

2 100
1 200
<expected> No

10 22
47 81 82 95 117 146 165 209 212 215
<expected> No


"""

n, s = map(int, input().split())
t = list(map(int, input().split()))
# print(t)

t_prev = 0
for t_now in t:
    if (t_now - t_prev) >= (s+0.5):
        print("No")
        exit()
    t_prev = t_now
print("Yes")
