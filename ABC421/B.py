#!/usr/bin/python3

# B - Fibonacci Reversed
# https://atcoder.jp/contests/abc421/tasks/abc421_b

# python ../validate.py B.py

# pytest tests/test_b.py
# pytest tests/test_b.py -k sample1

"""TEST_DATA
1 1
<expected> 415

3 7
<expected> 895

90701 90204
<expected> 9560800101

"""

import os

def f(x):
    x_str = str(x)

    ans = ""
    for i in range(len(x_str)):
        ans += x_str[len(x_str) - i - 1]
    return int(ans)

def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)

X, Y = map(int, input().split())

result = 0
for _ in range(2, 10):
    result = f(X + Y)
    X = Y
    Y = result
print(result)
