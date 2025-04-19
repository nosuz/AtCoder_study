#!/usr/bin/python3

"""TEST_DATA
6
1 3
1 1
1 15
2
1 3
2
<expected> 3 1
"""

import re

q = int(input())

que = []
placed = 0
for _ in range(q):
    query = input()
    if query.startswith("1 "):
        m = re.search(r'1 (\d+)', query)
        que.append(m.group(1))
    else:
        print(que[placed])
        placed += 1

if placed == 0:
    print()
