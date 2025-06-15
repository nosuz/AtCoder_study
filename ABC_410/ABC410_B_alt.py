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

1 3
1 0 0
<expected>1 1 1

2 4
0 0 0 0
<expected>1 2 1 2
"""


def full_scan(box):
    candidate = [0]

    p = 0
    v = box[p]
    for i in range(1, len(box)):
        if box[i] < v:
            p = i
            v = box[i]
            # reset
            candidate = [i]
        elif box[i] == v:
            candidate.append(i)
    return candidate


n, q = map(int, input().split())
x = list(map(int, input().split()))

box_count = [0 for _ in range(n)]
box_q = []

candidate = []

for i in x:
    if i == 0:
        if len(candidate) == 0:
            candidate = full_scan(box_count)

        min_p = candidate.pop(0) # pop at 0. default is -1 or at the last
        box_count[min_p] += 1
        box_q.append(min_p + 1)
    else:
        box_count[i - 1] += 1
        box_q.append(i)
        # update candidate
        if (i - 1) in candidate:
            candidate.remove(i - 1)

print(" ".join(map(str, box_q)))
