#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
4 2
2 4
6 8
3
1 3
3 7
1 5
<expected> 1 2 0

20 7
24 34
26 28
18 38
2 14
8 12
30 32
20 22
10
7 29
31 39
9 21
19 29
15 21
11 39
17 21
15 31
5 25
25 31
<expected> 3 3 4 1 2 2 2 3 3 1


"""

# nodes number = 2 * n
n, m = map(int, input().split())


lines = []
for _ in range(m):
    a, b = map(int, input().split())
    lines.append((a, b))

q = int(input())

counts = []
for _ in range(q):
    c, d = map(int, input().split())

    count = 0
    for line in lines:
        # LTE
        # if (line[0] < c) and (c < line[1] < d):
        #     # print(line)
        #     count += 1
        # elif (line[1] > d) and (c < line[0] < d):
        #     # print(line)
        #     count += 1

        # LTE
        crossing = 0
        if c < line[0] < d:
            crossing += 1
        if c < line[1] < d:
            crossing += 1
        count += credits % 2
    counts.append(count)

for count in counts:
    print(count)
