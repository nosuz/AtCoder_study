#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
5 4
2 1 2
3 3 4 5
3 1 2 5
1 3
1 3 2 5 4
<expected> 0 1 2 3 4

9 8
1 4
5 6 9 7 4 3
4 2 4 1 3
1 1
5 7 9 8 1 5
2 9 8
1 2
1 1
6 5 2 7 8 4 1 9 3
<expected> 0 0 1 1 1 2 4 6 8

"""

n, m = map(int, input().split())

items = [set() for _ in range(n + 1)]
for i in range(1, m + 1):
    dish = list(map(int, input().split()))
    for item in dish[1:]:
        items[item].add(i)
# print(items)

eat = list(map(int, input().split()))
# print(eat)

ok = [m]
ok_dishes = set()
for i in range(len(eat) - 1, 0, -1):
    item = eat[i]
    ok_dishes |= items[item]
    ok.append(m - len(ok_dishes))
# print(ok)
ok.reverse()
print(" ".join(list(map(str, ok))))
