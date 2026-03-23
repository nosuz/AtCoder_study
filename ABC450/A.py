#!/usr/bin/python3

# A - 3,2,1,GO
# https://atcoder.jp/contests/abc450/tasks/abc450_a

# python ../validate.py A.py

# pytest tests/test_a.py
# pytest tests/test_a.py -k sample1

"""TEST_DATA
9
<expected> 9,8,7,6,5,4,3,2,1

5
<expected> 5,4,3,2,1

1
<expected> 1

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())

ans = []
for i in range(N, 0, -1):
    ans.append(str(i))

print(",".join(ans))
