"""TEST_DATA
4
3 12 9 9

3
3 9 6

4
100 100 100 100

8
87 87 87 88 41 38 41 38

"""

r = 1
n = int(input())
p = map(int, input().split())
l = [(a, i) for i, a in enumerate(p)]
# print(l)

result = sorted(l, reverse=True, key=lambda x: x[0])

rank = []
prev = None
for i, t in enumerate(result):
    if t[0] != prev:
        r = i + 1
        prev = t[0]
    rank.append((t[1], r))
# print(rank)

for i in sorted(rank, reverse=False, key=lambda x: x[0]):
    print(i[1])
