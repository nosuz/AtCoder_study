"""TEST_DATA
3
3 1 2 3
4 1 2 2 1
6 1 2 3 4 5 6
<expected> 0.333333333333333

3
5 1 1 1 1 1
4 2 2 2 2
3 1 1 2
<expected> 0.666666666666667

"""

import itertools
from collections import defaultdict

n = int(input())

k = []
for _ in range(n):
    a = list(map(int, input().split()))
    faces = a[0]  # number of faces

    # count each numbers
    # _p = {}
    _p = defaultdict(lambda: 0)
    for i in a[1:]:
        num = str(i)
        # if num in _p:
        #     _p[num] += 1
        # else:
        #     _p[num] = 1
        _p[num] += 1  # default value is 0
    # calculate each P
    p = {k: v / faces for k, v in _p.items()}
    k.append(p)

max_p = 0
# make nC2
for k_a, k_b in itertools.combinations(k, 2):
    # intersection might reduce the number of loops
    keys = set(k_a.keys()) & set(k_b.keys())
    # P that two dices show the same number
    p_sum = 0
    for key in keys:
        # use default value if not having a key
        p_sum += k_a.get(key, 0) * k_b.get(key, 0)

    if p_sum > max_p:
        max_p = p_sum

# delta: less than 10^-8 is OK
print(f"{max_p:.15f}")
