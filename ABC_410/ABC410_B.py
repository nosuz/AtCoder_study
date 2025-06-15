#!/usr/bin/python3

# python3 validate.py sample.py

# B - Reverse Proxy
# https://atcoder.jp/contests/abc410/tasks/abc410_b

"""TEST_DATA
4 5
2 0 3 0 0
<expected> 2 1 3 4 1

3 7
1 1 0 0 0 0 0
<expected> 1 1 2 3 2 3 1

6 20
4 6 0 3 4 2 6 5 2 3 0 3 2 5 0 3 5 0 2 0
<expected> 4 6 1 3 4 2 6 5 2 3 1 3 2 5 1 3 5 4 2 6


"""

n, q = map(int, input().split())
x = list(map(int, input().split()))

box_count = [0 for _ in range(n)]
box_q = []

for i in x:
    if i == 0:
        min_v = box_count[0]
        min_p = 0
        for j in range(1, n):
            if box_count[j] < min_v:
                min_p = j
                min_v = box_count[j]
        box_count[min_p] += 1
        box_q.append(min_p + 1)
    else:
        box_count[i - 1] += 1
        box_q.append(i)

print(" ".join(map(str, box_q)))
