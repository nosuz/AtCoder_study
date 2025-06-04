#!/usr/bin/python3

# python3 validate.py sample.py
"""TEST_DATA
10 4
1 6
4 5
5 10
7 10
<expected> 1

5 2
1 2
3 4
<expected> 0

5 10
2 5
1 5
1 2
2 4
2 2
5 5
2 4
1 2
2 2
2 3
<expected> 3


"""

n, m = map(int, input().split())
# print(n, m)

wall = [0 for _ in range(n + 1)]
# (0) =1= (1) =2= (2) =3= (3) =4= (4) ... =n= (n)
for _ in range(m):
    l, r = map(int, input().split())
    wall[l - 1] += 1
    wall[r] -= 1
# print(wall)

result = []
temp = 0
for v in wall:
    temp += v
    result.append(temp)
# print(result)
print(sorted(result[0:-1])[0])
