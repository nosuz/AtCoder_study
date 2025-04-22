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

dishes = []
for _ in range(m):
    dish = list(map(int, input().split()))
    dishes.append(dish[1:])
# print(dishes)

eat = list(map(int, input().split()))
# print(eat)

edible = [0] * (n + 1)
for day in range(n):
    item = eat[day]
    edible[item] = day
# print(edible)

ok = [0] * n
for items in dishes:
    max_day = 0
    for item in items:
        edible_date = edible[item]
        if edible_date > max_day:
            max_day = edible_date
    # print(f"{items} -> {max_day}")
    ok[max_day] += 1

sum = 0
ok_num = []
for i in range(n):
    sum += ok[i]
    ok_num.append(sum)
print(" ".join(list(map(str, ok_num))))
