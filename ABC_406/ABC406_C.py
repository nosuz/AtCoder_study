#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
6
1 3 6 4 2 5
<expected> 2

7
7 1 3 6 4 2 5
<expected> 2

6
1 2 3 4 5 6
<expected> 0

12
11 3 8 9 5 2 10 4 1 6 12 7
<expected> 4

7
1 3 2 4 6 5 7
<expected> 4

"""

import os


def debug(*args):
    if os.environ.get("DEBUG") in ("1", "true", "True", "yes"):
        print(*args)


N = int(input())
P = list(map(int, input().split()))

# A_1 < A_2 なので、常に <>, >< の順番
delta = ["<" if (P[i] - P[i - 1]) > 0 else ">" for i in range(1, N)]
debug(delta)

ans = 0
a = 0
while a < (N - 1):
    debug(a)
    if delta[a] != "<":
        a += 1
        continue

    tilde = [0, 0]  # [<>, ><]
    for b in range(a + 1, N - 1):
        if delta[b - 1] == "<" and delta[b] == ">":
            tilde[0] = b - 1
        elif delta[b - 1] == ">" and delta[b] == "<":
            tilde[1] = b

        debug(f"a:{a},b:{b},~:{tilde}")
        if tilde[0] < tilde[1]:
            extend = tilde[1]
            for c in range(tilde[1], N - 1):
                if delta[c] == "<":
                    extend = c
                else:
                    break

            # ~の数を計算
            ans += (tilde[0] - a + 1) * (extend - tilde[1] + 1)
            # 次の~グループを探す
            a = tilde[1]
            debug(f"next(find):{a}")
            break
    else:
        # ~が見つからなかった。
        debug("not found")
        break
print(ans)
