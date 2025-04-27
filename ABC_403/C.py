#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
2 3 5
1 1 2
3 1 1
3 1 2
2 2
3 2 3
<expected> No Yes Yes

5 5 10
2 2
3 4 4
1 1 1
1 4 1
1 4 2
1 4 4
1 2 4
3 3 2
3 5 4
3 2 1
<expected> No No No Yes

"""


n, m, q = map(int, input().split())

all_granted = [False] * (n + 1)
granted = [set() for _ in range(n + 1)]
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        granted[query[1]].add(query[2])
    elif query[0] == 2:
        all_granted[query[1]] = True
    else:
        # print(query[1])
        # print(all_granted)
        # print(granted)
        if all_granted[query[1]] or (query[2] in granted[query[1]]):
            print("Yes")
        else:
            print("No")
