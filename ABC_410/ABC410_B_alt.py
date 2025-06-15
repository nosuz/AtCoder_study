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


def full_scan(box):
    p = 0
    p_v = box[p]
    for i in range(1, len(box)):
        if box[i] < p_v:
            p = i
            p_v = box[i]
    return p, p_v


def scan_same(box, p, v):
    found = False
    for i in range(p, len(box)):
        if box[i] == v:
            return True, i
    return False, 0


n, q = map(int, input().split())
x = list(map(int, input().split()))

box_count = [0 for _ in range(n)]
box_q = []

had_zero = False
min_p = 0
min_v = box_count[min_p]
for i in x:
    if i == 0:
        if had_zero:
            result, min_p = scan_same(box_count, min_p, min_v)
            if result:
                # found
                box_count[min_p] += 1
                box_q.append(min_p + 1)
            else:
                min_p, min_v = full_scan(box_count)
                box_count[min_p] += 1
                box_q.append(min_p + 1)

        else:
            had_zero = True

            min_p, min_v = full_scan(box_count)
            box_count[min_p] += 1
            box_q.append(min_p + 1)
    else:
        box_count[i - 1] += 1
        box_q.append(i)

print(" ".join(map(str, box_q)))
