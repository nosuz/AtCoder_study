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

from operator import itemgetter


def generate_sort_key(eat):
    return lambda x: tuple(-x[i] for i in reversed(eat))


n, m = map(int, input().split())

dishes = []
for i in range(m):
    dish = list(map(int, input().split()))
    items = [False] * (n + 1)
    for i in dish[1:]:
        items[i] = True
    dishes.append(items)
    # items = set(dish[1:])
    # dishes.append([True if i in items else False for i in range(n + 1)])
# print(dishes)

eat = list(map(int, input().split()))
# print(eat)
sorted_dishes = sorted(dishes, key=generate_sort_key(eat), reverse=True)
# for dish in sorted_dishes:
#     print(dish)

mask = [True] * (n + 1)
index = 0
edible = []
for item in eat:
    mask[item] = False
    # print(mask)
    while True:
        for a, b in zip(mask, sorted_dishes[index]):
            if a and b:
                break
        else:
            index += 1
            if index == len(sorted_dishes):
                break
            continue

        break
    edible.append(index)
print(" ".join(map(str, edible)))
