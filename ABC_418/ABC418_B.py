#!/usr/bin/python3

# python3 validate.py sample.py

# B - You're a teapot
# https://atcoder.jp/contests/abc418/tasks/abc418_b

"""TEST_DATA
attitude
<expected> 0.50000000000000000

ottottott
<expected> 0.66666666666666667

coffeecup
<expected> 0.00000000000000000


"""

import re
import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


S = input()

m = re.search(r'(t.+t)', S)
if m:
    s = m.groups()[0]
    p_max = 0
    for i in range(len(s)):
        for j in range(i+2, len(s)):
            s_ = s[i:j+1]
            if (len(s_) > 2) and (s_[0] == 't') and (s_[-1] == 't'):
                debug(s_)
                t_count = s_.count('t')
                p = (t_count - 2)/(len(s_) - 2)
                debug(p)
                if p_max < p:
                    p_max = p
    print(p_max)
else:
    print(0)
