#!/usr/bin/python3

# C - Reindeer and Sleigh 2
# https://atcoder.jp/contests/abc437/tasks/abc437_c

# python ../validate.py C.py

# pytest tests/test_c.py
# pytest tests/test_c.py -k sample1

"""TEST_DATA
3
3
3 1
4 1
5 9
5
1000000000 1
1000000000 1
1000000000 1
1000000000 1
1000000000 1
10
133180711 458704923
531424946 225863856
141986070 637075158
500770732 289806469
502866767 408857335
559714289 569084545
287444582 992432993
559747907 753133304
432846188 949871298
727072164 756020367
<expected> 2
0
6

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


T = int(input())
for t in range(T):
    N = int(input())
    weight = 0
    tonaki = []
    for n in range(N):
        W, P = map(int, input().split())
        weight += W
        tonaki.append({"weight": W, "power": P})

    # P-Wではなく、P+Wでsortするのが肝心。
    tonaki.sort(key=lambda x: x["power"] + x["weight"], reverse=True)
    # debug(tonaki)

    for n in range(N):
        deer = tonaki[n]
        weight -= deer["power"] + deer["weight"]
        if weight <= 0:
            print(N - (n+1))
            break
    else:
        print(0)
