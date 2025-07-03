#!/usr/bin/python3

# python3 validate.py sample.py

# C - Giant Domino
# https://atcoder.jp/contests/abc412/tasks/abc412_c

"""TEST_DATA
3
4
1 3 2 5
2
1 100
10
298077099 766294630 440423914 59187620 725560241 585990757 965580536 623321126 550925214 917827435
<expected> 4 -1 3

2
4
1 2 2 4
4
2 2 2 4
<expected> 3 2

1
3
2 2 2
<expected> 2

1
4
2 2 2 4
<expected> 2

1
2
2 4
<expected> 2

1
2
2 2
<expected> 2

1
5
1 2 2 2 6
<expected> -1

1
5
1 2 4 6 6
<expected> 4

"""

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    s_1 = s[0]
    s_n = s[-1]

    # simplify S items and sort them
    items = [s_1] + sorted(set(filter(lambda x: (x > s_1)
                           and (x < s_n), s[1:-1]))) + [s_n]
    # print(items)

    placed = [s_1]
    start_index = 0
    start_size = s_1
    if (items[0] * 2) < items[1]:
        # print("X")
        print(-1)
        continue

    # start from 2 beacause the item[1] is already confirmed above.
    for i in range(2, len(items)):
        if (start_size * 2) < items[i]:
            # failed to push over a domino.
            # print(f"{start_size}x{items[i]}({i})")
            start_index = i - 1
            # print(f"start: {start_index}")
            start_size = items[start_index]
            placed.append(start_size)

            # confirm pushable over the next.
            if (start_size * 2) < items[i]:
                break
        else:
            # print(f"{start_size}-{items[i]}({i})")
            pass
    else:
        # No break in for-loop.
        placed.append(s_n)
        # print(placed)
        print(len(placed))
        continue
    # failed to push over the next dominos.
    print(-1)
